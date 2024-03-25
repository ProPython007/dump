import socket


port = 50000
host = "127.0.0.1"
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("Socket binded to %s" % port)
print("Server is listening...")

def search_arp_table():
    with open('/proc/net/arp', 'r') as file:
        lines = file.readlines()
    
    table = []
    for line in lines:
        table.append(line.split())
    
    ARP_table = {}
    for line in table:
        if line[0] != 'IP':
            ARP_table[line[0]] = line[3]
    
    return ARP_table


while True:
    data, client_address = server.recvfrom(2048)
    print("Message from client:", data.decode())
    if data.decode() == 'bye':
        break
 
    str1 = data.decode()
    arp_table = search_arp_table()
    if str1 in arp_table:
        str2 = arp_table[str1]
    else:
        str2 = "IP address not found"

server.sendto(str2.encode(), client_address)
print("Connection closed from client")
server.close()
