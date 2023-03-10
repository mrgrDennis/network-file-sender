import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5000  # Arbitrary non-privileged port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to a specific port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen(1)
    print(f'Waiting for a connection on port {PORT}...')

    # Accept a connection from a client
    conn, addr = s.accept()
    print(f'Connected by {addr}')

    # Receive the filename from the client
    filename = conn.recv(1024).decode()
    print(f'Receiving file: {filename}')

    # Open the file for writing
    with open(filename, 'wb') as f:
        # Receive the file data in chunks
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print('File received successfully')
