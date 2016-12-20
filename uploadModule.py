import os
import pathconverter

CRLF="\r\n"
BUFF=1024

def upload(socket_client, currentDirectory, path):
    print 'masuk uplot'
    data=""
    temp = path
    newPartition = temp.partition(" ")
    newPath = newPartition[0]
    size, delimiter, body=newPartition[2].partition("\r\n\r\n")
    newSize = size.partition(" ")[0]
    with open(newPath, 'wb') as fileuploaded:
        data = data + body
        filereceived = len(data)
        fileuploaded.write(data)
        while int(filereceived)<int(newSize):
            temp=socket_client.recv(BUFF)
            fileuploaded.write(temp)
            filereceived+=len(temp)
        fileuploaded.close()