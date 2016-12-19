import os
import pathconverter

CRLF="\r\n"

def download(socket_client, currentDirectory, path):
	print 'sampe sini'
	joinPath = os.path.join(currentDirectory, path)
	if os.path.exists(joinPath):
		filesize=os.path.getsize(path)
		socket_client.sendall(str(filesize)+"\r\n"+"\r\n")
		with open(path,"rb") as file:
			data = file.read()
			socket_client.sendall(data)
	else:
		socket_client.sendall("\r\n")