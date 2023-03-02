import time
import socket

HOST = 'localhost'  # IP address or hostname of receiver
PORT = 12345        # Port number of receiver
BEAT_INTERVAL = 1   # Interval between heartbeat messages, in seconds

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to receiver
s.connect((HOST, PORT))

while True:
    # Send heartbeat message
    s.sendall(b'beat')

    # Log heartbeat message
    print(f'Sent beat at {time.time()}')

    # Wait for interval before sending next heartbeat
    time.sleep(BEAT_INTERVAL)