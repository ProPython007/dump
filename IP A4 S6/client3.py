import socket

port = 6963
portClient = 8003
host = "127.0.0.3"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, portClient))
client.connect((host, port))

while True:	
	data = input("\nEnter your message: ")
	client.send(data.encode())
	if data.lower() == 'quit':
		break
	recieved_data = client.recv(2048)
	print("Message from server:", recieved_data.decode())
		
print("Connection closed from server")
client.close()