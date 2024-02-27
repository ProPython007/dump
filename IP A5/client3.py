import socket
import pickle


port = 6967
portClient = 8007
host = "127.0.0.7"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, portClient))
client.connect((host, port))

while True:	
	data = input("\nEnter url to scrape followed by the depth (link, depth): ")
	client.send(data.encode())
	if data.lower() == 'quit':
		break
	recieved_data = client.recv(65536)
	data = pickle.loads(recieved_data)
	print("Message from server:")
	for k, v in data.items():
		print(f'\nLevel {k} :')
		print(v)
		
print("Connection closed from server")
client.close()