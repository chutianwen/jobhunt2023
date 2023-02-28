import socket
import threading
import sys
import time

BUFSIZE = 1024
SERVER_LIST = [('localhost', 8888), ('localhost', 8889)]
lock = threading.Lock()

class Client:
    def __init__(self, name):
        self.name = name
        self.socket = None
        self.server_index = 0
        self.lock = threading.Lock()
        self.connect_to_server()

    def connect_to_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = SERVER_LIST[self.server_index]
        try:
            self.socket.connect(server_addr)
            # lock.acquire()
            with self.lock:
                self.socket.send(f"JOIN {self.name}".encode('utf-8'))
            # lock.release()
            print(f"Connected to {server_addr}")
        except ConnectionRefusedError:
            print(f"Failed to connect to {server_addr}")
            self.reconnect()
            return

        # Start a separate thread to listen for server pings
        ping_thread = threading.Thread(target=self.heart_beat)
        ping_thread.daemon = True
        ping_thread.start()

        receive_thread = threading.Thread(target=self.handle_incoming_messages)
        receive_thread.start()

        # Start the main client loop
        self.run()

    def reconnect(self):
        # Try to connect to the next server in the list
        self.server_index = (self.server_index + 1) % len(SERVER_LIST)
        print(f'Current server: {self.server_index}')
        # self.server_index = 0
        self.connect_to_server()

    def heart_beat(self):
        # avoid sending connection name from 'x' to 'xPING', if heart_beat gets executed same time to
        # main thread, then the PING will be buffered with x, then server will get name as xPING.
        # time.sleep(0.01)
        while True:
            try:
                # lock.acquire()
                with self.lock:
                    self.socket.send(b'PING')
                # lock.release()
                self.socket.settimeout(60.0)
                time.sleep(15)
            except socket.timeout:
                print(f"Server {SERVER_LIST[self.server_index]} timed out, switching to next server")
                self.reconnect()
            except ConnectionResetError:
                print(f"Server {SERVER_LIST[self.server_index]} reset connection, switching to next server")
                self.reconnect()
            except OSError:
                print(f"Server {SERVER_LIST[self.server_index]} closed connection, switching to next server")
                self.reconnect()


    def run(self):
        while True:
            msg = input("> ")
            if not msg:
                break

            if ':' in msg:
                recipient, msg = msg.split(':', 1)
                # lock.acquire()
                with self.lock:
                    self.send_direct(recipient, msg)
                # lock.release()
            else:
                # lock.acquire()
                with self.lock:
                    self.send_message(msg)
                # lock.release()

    def send_message(self, msg):
        try:
            self.socket.sendall(f"MESSAGE {msg}".encode('utf-8'))
        except ConnectionError:
            print("Failed to send message")
            self.connect_to_server()

    def send_direct(self, recipient, msg):
        try:
            self.socket.sendall(f"DIRECT {recipient} {msg}".encode('utf-8'))
        except ConnectionError:
            print("Failed to send message")
            self.connect_to_server()

    # Define function to handle incoming messages from server
    def handle_incoming_messages(self):
        while True:
            try:
                data = self.socket.recv(BUFSIZE)
            except ConnectionResetError:
                print("Connection closed to server")
                self.reconnect()

            if not data:
                print(f'No data for name: {self.name}')
            elif data == b'PONG':
                continue
            else:
                print(data.decode())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py <name>")
        sys.exit(1)

    client = Client(sys.argv[1])
