from bs4 import BeautifulSoup
import requests
import socket
import pickle
import re


import warnings
warnings.filterwarnings("ignore")


def scrape_links(url_to_scrape):
	parsed_links = []
	try:
		source = requests.get(url_to_scrape).text
		soup = BeautifulSoup(source, 'html.parser')

		for link in soup.find_all('a', attrs={'href': re.compile("^https://")}): 
			parsed_links.append(link.get('href'))

	except Exception as err:
		pass

	return parsed_links



port = 6967
host = "127.0.0.7"

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

	url, depth = c_msg.split(',')

	urls_parsed = {}
	for i in range(int(depth)):
		urls_parsed[i+1] = []

	for i in range(1, int(depth)+1):
		if i == 1:
			urls_parsed[i] = scrape_links(url)
		else:
			for link in urls_parsed[i-1]:
				urls_parsed[i].extend(scrape_links(link))

	data_stream = pickle.dumps(urls_parsed)
	
	conn.send(data_stream)

print("Connection closed from client")
conn.close()