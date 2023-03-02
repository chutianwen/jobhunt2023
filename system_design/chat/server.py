import socket
import threading

# Define constants
HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024

# Define function to handle incoming client connections
def handle_client(sock, addr, clients):
    # Get client username
    username = sock.recv(BUFSIZE).decode()

    # Add client to list of clients
    clients.append((sock, username))

    # Send welcome message to new client
    message = f'Welcome, {username}!'
    sock.sendall(message.encode())

    # Loop to receive and relay messages
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        # Find recipient client based on message prefix
        recipient_username = data.decode().split(':')[0]
        recipient_sock = None
        for client in clients:
            if client[1] == recipient_username:
                recipient_sock = client[0]
                break
        # Send message to recipient client
        if recipient_sock is not None:
            recipient_sock.sendall(data)

    # Remove client from list of clients
    clients.remove((sock, username))

    # Close connection
    sock.close()

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen()

# Create list to store connected clients
clients = []

# Loop to handle incoming client connections
while True:
    conn, addr = s.accept()
    print(f'Connection established with {addr[0]}:{addr[1]}')
    thread = threading.Thread(target=handle_client, args=(conn, addr, clients))
    thread.start()

# Close server socket
s.close()