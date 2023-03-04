import socket
import pickle
from functools import lru_cache


BUFSIZE = 1024
SERVER_HOST = 'localhost'
SERVER_PORT = 8888


class CacheServer:
    def __init__(self, host, port, max_size=1024):
        self.host = host
        self.port = port
        self.max_size = max_size
        self.cache = {}

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
            s.bind((self.host, self.port))
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


if __name__ == '__main__':
    # Instantiate a CacheServer object with capacity of 100 and LRU eviction policy
    server = CacheServer(host=SERVER_HOST, port=SERVER_PORT)
    server.start()