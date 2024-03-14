import socket


PORT = 5050
DISCONNECT_MESSAGE = "bye"
SERVER = "172.16.2.146"
# CLIENT_HOST = "127.0.0.1"
# CLIENT_PORT = 5051

ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.bind((CLIENT_HOST, CLIENT_PORT))
client.connect(ADDR)


def send(msg):
    message = msg.encode()
    client.send(message)
    print(client.recv(204800).decode())


_temp = ''
while _temp != DISCONNECT_MESSAGE:
    _temp = input('\nEnter your msg to send to server (bye to close): ')
    send(_temp)