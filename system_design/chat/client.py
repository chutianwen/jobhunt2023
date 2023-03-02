import socket
import threading

# Define constants
HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024

# Define function to handle incoming messages from server
def handle_incoming_messages(sock):
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        print(data.decode())

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
s.connect((HOST, PORT))

# Get username from user
username = input('Enter your username: ')

# Send username to server
s.sendall(username.encode())

# Start thread to handle incoming messages from server
thread = threading.Thread(target=handle_incoming_messages, args=(s,))
thread.start()

# Loop to send messages
while True:
    message = input('> ')
    s.sendall(message.encode())

# Close connection
s.close()