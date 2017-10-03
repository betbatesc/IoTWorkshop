from bluetooth import *

server_address = "B8:27:EB:F9:6E:78"
port = 1

sock = BluetoothSocket(RFCOMM)
sock.connect((server_address, port))

sock.send("Hello!")

sock.close()
