import socket
import pickle


BUFSIZE = 1024
SERVER_HOST = 'localhost'
SERVER_PORT = 8888


class CacheClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def set(self, key, value):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(pickle.dumps(("SET", key, value)))
            response = s.recv(1024)
            return pickle.loads(response)

    def get(self, key):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(pickle.dumps(("GET", key)))
            response = s.recv(1024)
            return pickle.loads(response)


if __name__ == '__main__':

    # Instantiate a CacheClient object
    client = CacheClient(host=SERVER_HOST, port=SERVER_PORT)

    # Set a key-value pair in the cache through the client
    client.set('key1', 'value1')

    # Retrieve the value of the key from the server through the client
    value1 = client.get('key1')

    # Print the retrieved value
    print(value1)  # 'value1'

    # Set another key-value pair in the cache through the client
    client.set('key2', 'value2')

    # Try to retrieve a non-existent key from the server through the client
    value3 = client.get('key3')

    # Print the retrieved value (should be None)
    print(value3)  # None