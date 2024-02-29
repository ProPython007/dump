import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_address = ('localhost', 8002)
server_socket.bind(server_address)

print('\nUDP server is listening...')

while True:
    # Receive message from client
    data, client_address = server_socket.recvfrom(1024)
    
    # Print received message and client address
    c_msg = data.decode()
    print(f"\nReceived '{c_msg}' from {client_address}")
    
    if c_msg == 'bye':
        break

    if len(c_msg) % 2 != 0: server_socket.sendto(c_msg[::2].encode(), client_address)
    else: server_socket.sendto(c_msg[1::2].encode(), client_address)
    
    # Echo the message back to the client
    # server_socket.sendto(data, client_address)

print("\nConnection closed from client!")
server_socket.close()