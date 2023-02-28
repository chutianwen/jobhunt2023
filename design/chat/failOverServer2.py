import socket
import threading

SERVER_HOST = 'localhost'
SERVER_PORT = 8889

class Server:
    def __init__(self):
        self.clients = {}
        self.server_socket = None
        self.start_server()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((SERVER_HOST, SERVER_PORT))
        self.server_socket.listen()

        print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Accepted connection from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.daemon = True
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
            except ConnectionResetError:
                print("Connection closed by client")
                break

            if not data:
                print("Connection closed by client")
                break

            print(f'client names:{self.clients}')
            print(f'Incoming data: {data}')
            if data == b'PING':
                print("heart beating")
                client_socket.sendall(b'PONG')
            else:
                message = data.decode('utf-8').strip()
                print(f'Incoming message: {message}')
                if message.startswith("JOIN"):
                    name = message.split()[1]
                    self.clients[name] = client_socket
                    print(f"{name} joined the chat")
                elif message.startswith("MESSAGE"):
                    msg = message.split(' ', 1)[1]
                    self.broadcast_message(msg)
                elif message.startswith("DIRECT"):
                    recipient, msg = message.split(' ', 2)[1:]
                    print(f'send direct message: {msg} to recipient: {recipient}')
                    self.send_direct_message(recipient, msg)
                else:
                    print(f"Unknown message: {message}")

        # client_socket.close()

    def broadcast_message(self, message):
        for name, client_socket in self.clients.items():
            try:
                client_socket.sendall(f"Broadcast: {message}".encode('utf-8'))
            except ConnectionError:
                print(f"Failed to send message to {name}")
                del self.clients[name]

    def send_direct_message(self, recipient, message):
        if recipient not in self.clients:
            print(f"Recipient {recipient} not found")
            return

        try:
            self.clients[recipient].sendall(f"{recipient}: {message}".encode('utf-8'))
        except ConnectionError:
            print(f"Failed to send direct message to {recipient}")
            del self.clients[recipient]


if __name__ == '__main__':
    server = Server()
