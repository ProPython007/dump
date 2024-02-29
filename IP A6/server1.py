import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_address = ('localhost', 8001)
server_socket.bind(server_address)

print('\nUDP server is listening...')

while True:
    # Receive message from client
    data, client_address = server_socket.recvfrom(1024)
    
    # Print received message and client address
    print(f"\nReceived '{data.decode()}' from {client_address}")
    
    # Echo the message back to the client
    # server_socket.sendto(data, client_address)