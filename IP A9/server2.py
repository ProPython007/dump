import socket

port = 50000
host = "127.0.0.1"
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("Socket binded to %s" % port)
print("Server is listening...")


def search_rarp_table():
    with open('/proc/net/arp', 'r') as file:
        lines = file.readlines()
    table = []
    
    for line in lines:
        table.append(line.split())
    RARP_table = {}
    
    for line in table:
        if line[0] != 'IP':
            RARP_table[line[3]] = line[0]

    return RARP_table


while True:
    data, client_address = server.recvfrom(2048)
    print("Message from client:", data.decode())
    if data.decode() == 'bye':
        break

    str1 = data.decode()
    rarp_table = search_rarp_table()
    if str1 in rarp_table:
        str2 = rarp_table[str1]
    else:
        str2 = "MAC address not found"
    
    server.sendto(str2.encode(), client_address)
    
print("Connection closed from client")
server.close()