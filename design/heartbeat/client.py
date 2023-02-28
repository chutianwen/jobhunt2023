import socket

# Define constants
HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
s.connect((HOST, PORT))

# Loop to send and receive messages
while True:
    # Send message to server
    message = input('> ')
    s.sendall(message.encode())

    # Receive response from server
    data = s.recv(BUFSIZE)
    print(f'Received: {data.decode()}')

# Close connection
s.close()