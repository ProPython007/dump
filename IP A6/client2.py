import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 8002)

while True:
    message = input("\nEnter message to send to server: ")

    # Send data to server
    client_socket.sendto(message.encode(), server_address)
    
    if message == 'bye': break
    
    # Receive response from server
    data, server = client_socket.recvfrom(1024)
    
    print(f"Received '{data.decode()}' from server")

print("\nConnection closed from server!")
client_socket.close()