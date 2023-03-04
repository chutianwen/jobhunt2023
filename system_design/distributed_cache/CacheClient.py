import socket
import sys
sys.path.append('../..')

import threading
import time
import pickle


BUFSIZE = 1024
MESSAGE_SPLITTER = b'\n'
SERVER_HOST = 'localhost'
SERVER_PORT = 8888

HEART_BEAT_TIME_GAP = 60
REPORT_STATUS_TIMEOUT = 60

SET_MESSAGE = 'SET'
GET_MESSAGE = 'GET'


class CacheClient:
    def __init__(self, coordinator_host, coordinator_port):
        self.coordinator_host = coordinator_host
        self.coordinator_port = int(coordinator_port)
        self.coordinator_address = (self.coordinator_host, self.coordinator_port)
        self.coordinator_socket = None
        self.consistent_hash = None
        self._start_server()
        self._run()

    def _run(self):
        while True:
            msg = input('Please input operation [SET|GET]>').upper()

            if msg == SET_MESSAGE:
                key = input('Please input key>')
                value = input('Please input value>')
                message = pickle.dumps((SET_MESSAGE, key, value))
                response = self._send_to_cache_server(key, message)
                print(f'Response from set: {response}')
            elif msg == GET_MESSAGE:
                key = input('please input key>')
                message = pickle.dumps((GET_MESSAGE, key))
                response = self._send_to_cache_server(key, message)
                print(f'Response from get: {response}')
            else:
                print(f'Unknown input, please do it again!')


    def _start_server(self):
        self.connect_to_coordinator()

        report_status_thread = threading.Thread(target=self._report_status)
        report_status_thread.daemon = True
        report_status_thread.start()


    def connect_to_coordinator(self):
        try:
            self.coordinator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.coordinator_socket.connect(self.coordinator_address)
            self.coordinator_socket.send(f'JOIN cache client\n'.encode('utf-8'))
            print(f'Connected to {self.coordinator_address}')

            # Start a separate thread to heartbeat coordinator
            heartbeat_coordinator_thread = threading.Thread(target=self._heart_beat_coordinator)
            heartbeat_coordinator_thread.daemon = True
            heartbeat_coordinator_thread.start()

            # Start a separate thread to receive messages from coordinator
            message_from_coordinator_thread = threading.Thread(target=self._handle_message_from_coordinator)
            message_from_coordinator_thread.daemon = True
            message_from_coordinator_thread.start()

        except ConnectionResetError:
            print(f'Failed to connect to {self.coordinator_address}')
            # self.connect_to_coordinator()

    def _handle_message_from_coordinator(self):
        while True:
            try:
                data = self.coordinator_socket.recv(BUFSIZE)
            except ConnectionResetError:
                print('Connection closed to server')
                break

            if not data:
                print('Connection closed to server')
                break

            # print(f'\n\nIn coming data:{data}')
            messages = data.rstrip(MESSAGE_SPLITTER).split(MESSAGE_SPLITTER)

            for message in messages:
                # print(f'message from coordinator: {message}')
                if message == b'PONG':
                    print(f'Receive heartbeat back from coordinator')
                elif message.startswith(b'map:'):
                    message = message.lstrip(b'maps:')
                    # print(f'message to pick load:{message}')
                    self.consistent_hash = pickle.loads(message)
                    # print(f'Successfully load the updated consistent hash from coordinator')
                else:
                    print(f"Unknown message: {message}")

        self.coordinator_socket.close()


    def _heart_beat_coordinator(self):
        while True:
            try:
                self.coordinator_socket.send(b'PING\n')
                time.sleep(HEART_BEAT_TIME_GAP)
            except socket.timeout:
                print(f"Coordinator server timed out, reconnect")
                # self.connect_to_coordinator()
                break

            except ConnectionResetError:
                print(f"Coordinator server reset error, reconnect")
                # self.connect_to_coordinator()
                break

            except OSError:
                print(f"Coordinator server closed connection, reconnect")
                # self.connect_to_coordinator()
                break

    def _get_cache_server_socket(self, key):
        cache_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if self.consistent_hash:
            virtual_node, node = self.consistent_hash.get_node(key)
            host, port = node.split(':')
            cache_server_socket.connect((host, int(port)))
            return cache_server_socket
        else:
            print(f'[Warn] Consistent_hash is empty')

    def _send_to_cache_server(self, key, message):
        cache_server_socket = self._get_cache_server_socket(key)

        try:
            cache_server_socket.sendall(message)
            response = cache_server_socket.recv(1024)
            loaded_response =  pickle.loads(response)
        except Exception as e:
            print(f'An error occurred while requesting cache server:{e}')
            loaded_response = None

        cache_server_socket.close()
        return loaded_response

    def _report_status(self):
        while True:
            print('\n'*2)
            print(f'==========Report status==========')
            print(f'Current consistent hash ring: {self.consistent_hash}')
            print(f'==========End report==========')
            time.sleep(REPORT_STATUS_TIMEOUT)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: python client.py <port>")
        sys.exit(1)

    server = CacheClient(coordinator_host=SERVER_HOST, coordinator_port=sys.argv[1])