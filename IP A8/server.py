import socket
import threading


PORT = 5050
SERVER = "172.16.2.146" #socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "bye"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"\n[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(204800).decode()
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"Client @[{addr}] sends: {msg}")
        conn.send("Msg received by server!".encode())

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=((conn, addr)))
        thread.start()
        print(f"\n[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("\n[STARTING] server is starting...")
start()