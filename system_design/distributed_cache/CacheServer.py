from functools import lru_cache
import pickle
import socket
import sys
import threading
import time
sys.path.append('../..')
from system_design.distributed_cache.common import *


class CacheServer:
    def __init__(self, coordinator_host, coordinator_port, max_size=1024):
        self.coordinator_host = coordinator_host
        self.coordinator_port = int(coordinator_port)
        self.coordinator_address = (self.coordinator_host, self.coordinator_port)

        # hydrated during connect_to_coordinator
        self.coordinator_socket = None
        self.cache_server_host = None
        self.cache_server_port = None

        self.max_size = max_size
        self.cache = {}
        self._connect_coordinator()
        self._start_monitor()

    def _connect_coordinator(self):
        self.coordinator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.coordinator_socket.connect(self.coordinator_address)
            self.cache_server_host, self.cache_server_port = self.coordinator_socket.getsockname()

            self.coordinator_socket.send(f'JOIN cache server\n'.encode('utf-8'))
            print(f'Connected to {self.coordinator_address}')

            # Start a separate thread to listen for server pings
            ping_thread = threading.Thread(target=self._heart_beat,
                                           args=(self.coordinator_socket,))
            ping_thread.daemon = True
            ping_thread.start()

        except ConnectionResetError:
            print(f'Failed to connect to {self.coordinator_address}')
            # self.connect_to_coordinator()

    def _start_monitor(self):
        report_status_thread = threading.Thread(target=self._report_status)
        report_status_thread.daemon = True
        report_status_thread.start()

    def _heart_beat(self, coordinator_socket):
        while True:
            try:
                coordinator_socket.send(b'PING' + MESSAGE_SPLITTER)
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

        coordinator_socket.close()

    @lru_cache(maxsize=None)
    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            self.evict()
        self.cache[key] = value
        return "OK"

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return None

    def evict(self):
        oldest_key = None
        for key in self.cache:
            if oldest_key is None or self.cache[key]["last_accessed"] < self.cache[oldest_key]["last_accessed"]:
                oldest_key = key
        del self.cache[oldest_key]

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # print(self.cache_server_host, self.cache_server_port)
            s.bind((self.cache_server_host, self.cache_server_port))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    method, *args = pickle.loads(data)
                    if method == "SET":
                        response = self.set(*args)
                    elif method == "GET":
                        response = self.get(*args)
                    else:
                        response = "ERROR"
                    conn.sendall(pickle.dumps(response))

    def _report_status(self):
        while True:
            print('\n'*2)
            print(f'==========Report status==========')
            print(f'Current cache: {self.cache}')
            print(f'==========End report==========')
            time.sleep(REPORT_STATUS_TIMEOUT)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py <name>")
        sys.exit(1)

    # Instantiate a CacheServer object with capacity of 100 and LRU eviction policy
    server = CacheServer(coordinator_host=SERVER_HOST, coordinator_port=sys.argv[1])
    server.start()