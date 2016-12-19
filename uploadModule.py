import os
import pathconverter

CRLF="\r\n"
BUFF=1024

def upload(socket_client, currentDirectory, path):
	filesize=0
	filereceived=0
	data=""
	temp=socket_client.recv(BUFF)
	filesize, delimiter, body=temp.partition("\r\n\r\n")
	with open(path, 'wb') as fileuploaded:
		while int(filereceived)<int(filesize):
			temp=socket_client.recv(BUFF)
			fileuploaded.write(temp)
			filereceived+=len(temp)
		fileuploaded.close()