import socket
import threading

# Define constants
HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen()

# Define function to handle client connection
def handle_client(conn, addr):
    while True:
        # Receive message from client
        data = conn.recv(BUFSIZE)
        if not data:
            break

        # Print message from client
        print(f'{addr[0]}:{addr[1]} says: {data.decode()}')

        # Send message back to client
        conn.sendall(data)

    # Close connection
    conn.close()

# Accept two connections from clients
print('Waiting for connections...')
conn1, addr1 = s.accept()
print(f'Connection established with {addr1[0]}:{addr1[1]}')
conn2, addr2 = s.accept()
print(f'Connection established with {addr2[0]}:{addr2[1]}')

# Create threads to handle client connections
thread1 = threading.Thread(target=handle_client, args=(conn1, addr1))
# thread2 = threading.Thread(target=handle_client, args=(conn2, addr2))

# Start threads
thread1.start()
# thread2.start()

# Wait for threads to finish
thread1.join()
# thread2.join()

# Close server socket
s.close()
