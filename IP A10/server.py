import socket
import os

def handle_request(client_connection):
    request_data = client_connection.recv(1024).decode()

    if not request_data:
        return

    request_method = request_data.split()[0]
    request_path = request_data.split()[1]
    
    print(request_method, request_path)

    if request_path == '/' or request_path == '/home':
        request_path = '/index.html'
    if request_path == '/about':
        request_path = '/about.html'

    try:
        with open('.' + request_path, 'rb') as f:
            response_body = f.read()
        response_headers = f'HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {len(response_body)}\n\n'
    except FileNotFoundError:
        response_body = b'<h3>404 Not Found</h3>'
        response_headers = f'HTTP/1.1 404 Not Found\nContent-Type: text/html\nContent-Length: {len(response_body)}\n\n'

    response = response_headers.encode() + response_body
    client_connection.sendall(response)
    client_connection.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(1)
    print("Server listening on port 8000...")

    while True:
        client_connection, client_address = server_socket.accept()
        handle_request(client_connection)

if __name__ == '__main__':
    run_server()