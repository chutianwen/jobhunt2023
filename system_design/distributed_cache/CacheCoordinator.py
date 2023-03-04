import sys

sys.path.append('../..')

from system_design.utils.consistent_hash import ConsistentHash
from system_design.utils.node import Node, SMALL_SIZE
import pickle
import socket
import threading
import time

BUFSIZE = 1024
MESSAGE_SPLITTER = '\n'
SERVER_HOST = 'localhost'
SERVER_PORT = 8888
HEART_BEAT_TIMEOUT = 30

class CacheCoordinator:
    '''
    Role 1: After cacheClient connecting to cacheCoordinator, push the updated consistent hash map
    to the cacheClient.
    Role 2: Heartbeat between cache server, whenever there's cacheSever add/delete, update the consistent hash ring.
    '''

    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.consistent_hash_pre = None
        self.consistent_hash = None
        self.cache_clients = set()
        self.cache_servers = {}
        self._start_server()

    def _start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

        print(f"Server listening on {self.host}:{self.port}")

        push_map_thread = threading.Thread(target=self._push_map)
        push_map_thread.daemon = True
        push_map_thread.start()

        report_status_thread = threading.Thread(target=self._report_status)
        report_status_thread.daemon = True
        report_status_thread.start()

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"\n\nAccepted connection from {client_address}\n\n")
            client_thread = threading.Thread(target=self._handle_client, args=(client_socket, client_address,))
            client_thread.daemon = True
            client_thread.start()

    def _handle_client(self, client_socket, client_address):
        client_host, client_port = client_address
        pre_heart_beat_time = int(time.time())
        while True:
            cur_time_seconds = int(time.time())
            # print(cur_time_seconds, pre_heart_beat_time)
            if pre_heart_beat_time and cur_time_seconds - pre_heart_beat_time > HEART_BEAT_TIMEOUT:
                print('Connection closed due to timeout from heartbeat')
                break

            try:
                data = client_socket.recv(BUFSIZE)
            except ConnectionResetError:
                print("Connection closed by client")
                break

            if not data:
                print("Connection closed by client")
                break

            print(f"Incoming data: {data}")

            messages = data.decode('utf-8').strip().split(MESSAGE_SPLITTER)

            for message in messages:
                print(f'message: {message}')
                if message == 'PING':
                    print(f'Heartbeat from {client_socket}')
                    pre_heart_beat_time = cur_time_seconds
                    client_socket.sendall(b'PONG')
                elif message == 'JOIN cache client':
                    print(f'Join a cache client from: {client_address}')
                    self.cache_clients.add(client_socket)

                elif message == 'JOIN cache server':
                    print(f'Join a cache server from: {client_address}')
                    if client_socket not in self.cache_servers:
                        self.cache_servers[client_socket] = Node(id=f"{client_host}:{client_port}", size=SMALL_SIZE)
                        self._update_map()
                else:
                    print(f"Unknown message: {message}")

        client_socket.close()

        # remove cache
        if client_socket in self.cache_servers:
            self.cache_servers.pop(client_socket)
            self._update_map()

        # remove cache_client
        if client_socket in self.cache_clients:
            self.cache_clients.remove(client_socket)

    def _update_map(self):
        nodes = list(self.cache_servers.values())
        # Make sure order is same
        nodes.sort(key=lambda node: node.id)
        self.consistent_hash = ConsistentHash(nodes=nodes, replicas=1)

    def _push_map(self):
        while True:
            if self.consistent_hash_pre != self.consistent_hash:
                print('\n'*2)
                for cache_client in self.cache_clients:
                    print(f'Push updated consistent hash map to cache_client: {cache_client}')
                    cache_client.sendall(pickle.dumps(self.consistent_hash))

                self.consistent_hash_pre = self.consistent_hash

            time.sleep(1)

    def _report_status(self):
        while True:
            print('\n'*2)
            print(f'==========Report status==========')
            print(f'Current connected cache client: {self.cache_clients}')
            print(f'Current connected cache servers: {self.cache_servers}')
            print(f'Current consistent hash: {self.consistent_hash}')
            print(f'==========End report==========')
            time.sleep(15)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py <port>")
        sys.exit(1)

    server = CacheCoordinator(host=SERVER_HOST, port=sys.argv[1])
