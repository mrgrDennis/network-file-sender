import socket

HOST = '192.168.1.100'  # The IP address of the server computer
PORT = 5000  # The same port as used by the server

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))

    # Prompt the user for the filename to send
    filename = input('Enter the filename to send: ')

    # Send the filename to the server
    s.sendall(filename.encode())

    # Open the file for reading
    with open(filename, 'rb') as f:
        # Send the file data in chunks
        while True:
            data = f.read(1024)
            if not data:
                break
            s.sendall(data)

    print('File sent successfully')
