from bluetooth import *

port = 1
backlog = 1

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", port))
server_sock.listen(backlog)

while True:
	client_sock, client_info = server_sock.accept()
	print("Connection accepted from ", client_info)
	data = client_sock.recv(1024)
	print("Received: ", data)

client_sock.close()
server_sock.close()
