import socket

port = 6962
host = "127.0.0.2"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("\nsocket binded to %s" % (port))

server.listen(2)
print("Socket is listening...")

# Accepting/Establishing connection from client.
conn, addr = server.accept()        
print('Got connection from', addr)

while True:
	recieved_data = conn.recv(2048)
	c_msg = recieved_data.decode()
	if c_msg.lower() == 'quit':
		break
	n = c_msg.count('1')
	conn.send(f'\nNo. of 1s in {c_msg} is: {n}, in binary: {bin(n)[2:]}'.encode())

print("Connection closed from client")
conn.close()