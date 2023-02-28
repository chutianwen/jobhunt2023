import time
import socket

HOST = 'localhost'  # IP address or hostname to bind to
PORT = 12345        # Port number to bind to

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen()

# Accept connection from sender
conn, addr = s.accept()

while True:
    # Receive heartbeat message
    data = conn.recv(1024)

    # Log heartbeat message
    print(f'Received beat at {time.time()}')

    # Send acknowledgement message
    conn.sendall(b'ack')