import pickle
import socket
import threading
import time
import sys
sys.path.append('../..')
from system_design.distributed_cache.common import *


class CacheClient:
    def __init__(self, coordinator_host, coordinator_port):
        self.coordinator_host = coordinator_host
        self.coordinator_port = int(coordinator_port)
        self.coordinator_address = (self.coordinator_host, self.coordinator_port)
        self.coordinator_socket = None
        self.consistent_hash = None

        # in parallel
        self._connect_coordinator()
        self._start_monitor()
        self._run()

    def _run(self):
        time.sleep(WARM_UP_TIME)
        while True:
            msg = input('Please input operation [SET|GET]>').upper()

            if msg == SET_MESSAGE:
                key = input('Please input key>')
                value = input('Please input value>')
                message = pickle.dumps((SET_MESSAGE, key, value))
                response = self._message_cache_server(key, message)
                print(f'Response from set: {response}')
            elif msg == GET_MESSAGE:
                key = input('please input key>')
                message = pickle.dumps((GET_MESSAGE, key))
                response = self._message_cache_server(key, message)
                print(f'Response from get: {response}')
            else:
                print(f'Unknown input, please do it again!')

    def _start_monitor(self):
        report_status_thread = threading.Thread(target=self._report_status)
        report_status_thread.daemon = True
        report_status_thread.start()

    def _connect_coordinator(self):
        try:
            self.coordinator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.coordinator_socket.connect(self.coordinator_address)

            self.coordinator_socket.send(b'JOIN cache client' + MESSAGE_SPLITTER)
            print(f'Connected to {self.coordinator_address}')

            # Start a separate thread to heartbeat coordinator
            heartbeat_coordinator_thread = threading.Thread(target=self._heart_beat_coordinator,
                                                            args=(self.coordinator_socket,))
            heartbeat_coordinator_thread.daemon = True
            heartbeat_coordinator_thread.start()

            # Start a separate thread to receive messages from coordinator
            message_from_coordinator_thread = threading.Thread(target=self._handle_message_from_coordinator,
                                                               args=(self.coordinator_socket,))
            message_from_coordinator_thread.daemon = True
            message_from_coordinator_thread.start()

        except ConnectionResetError:
            print(f'Failed to connect to {self.coordinator_address}')
            # self.connect_to_coordinator()

    def _handle_message_from_coordinator(self, coordinator_socket):
        while True:
            try:
                data = coordinator_socket.recv(BUFFER_SIZE)
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
                    print(f'\n\nReceive heartbeat back from coordinator')
                elif message.startswith(b'map:'):
                    message = message.lstrip(b'maps:')
                    # print(f'message to pick load:{message}')
                    self.consistent_hash = pickle.loads(message)
                    # print(f'Successfully load the updated consistent hash from coordinator')
                else:
                    print(f"\n\nUnknown message: {message}")

        self.coordinator_socket.close()

    def _heart_beat_coordinator(self, coordinator_socket):
        while True:
            try:
                coordinator_socket.send(b'PING' + MESSAGE_SPLITTER)
                time.sleep(HEART_BEAT_TIME_GAP)
            except coordinator_socket.timeout:
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

        coordinator_socket.close()

    def _get_cache_server_socket(self, key):
        cache_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if self.consistent_hash:
            virtual_node, node = self.consistent_hash.get_node(key)
            host, port = node.split(NODE_ID_SPLITTER)
            cache_server_socket.connect((host, int(port)))
            return cache_server_socket
        else:
            print(f'[Warn] Consistent_hash is empty')
            return None

    def _message_cache_server(self, key, message):
        cache_server_socket = self._get_cache_server_socket(key)
        if cache_server_socket:
            try:
                cache_server_socket.sendall(message)
                buffer = cache_server_socket.recv(BUFFER_SIZE)
                response = pickle.loads(buffer)
            except Exception as e:
                print(f'An error occurred while requesting cache server:{e}')
                response = None

            cache_server_socket.close()
            return response
        else:
            print(f'[Warn] Cache_server_socket is None')
            return None

    def _report_status(self):
        while True:
            print('\n'*2)
            print(f'==========Report status==========')
            print(f'Current consistent hash ring: {self.consistent_hash.ring if self.consistent_hash else None}')
            print(f'==========End report==========')
            time.sleep(REPORT_STATUS_TIMEOUT)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: python client.py <port>")
        sys.exit(1)

    server = CacheClient(coordinator_host=SERVER_HOST, coordinator_port=sys.argv[1])