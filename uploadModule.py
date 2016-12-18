import os
import pathconverter

def upload(socket_client, currentDirectory, path):
	joinPath = os.path.join(currentDirectory, path)
	if os.path.exists(joinPath):
		filesize=os.path.getsize(path)
		socket_client.sendall(str(filesize)+"\r\n"+"\r\n")
		with open(path,"r") as file:
			socket_client.sendall(file.read())
	else:
		socket_client.sendall("\r\n")