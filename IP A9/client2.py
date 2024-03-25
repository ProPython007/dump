import socket

port = 12345
host = "127.0.0.1"
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("Enter your message: ")
    client.sendto(data.encode(), (host, port))
    if data == 'bye':
        break
    received_data, server_address = client.recvfrom(2048)
    print("Message from server:", received_data.decode())
    
print("Connection closed from client")
client.close()