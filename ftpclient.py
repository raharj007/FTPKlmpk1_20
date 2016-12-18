import socket
import select
import sys

BUFF=1024

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect(('localhost', 5000))

#commands = ['USER raharjo\r\n', 'PASS 123\r\n', 'PWD\r\n', 'QUIT\r\n']

read_ready, write_ready, erro=select.select([socket_client],[],[],1)

for sock in read_ready:
    if(sock==socket_client):
        data=sock.recv(1024)
        print data

while True:
    try:
        cmd=raw_input()
        socket_client.sendall(cmd+"\r\n")
        if cmd.partition(" ")[0].upper()=="RETR":
            filesize=0
            filereceived=0
            data=""
            temp=socket_client.recv(BUFF)
            filesize, delimiter, body=temp.partition("\r\n\r\n")
            data=data+body
            #print temp.partition("\r\n\r\n")
            filereceived=len(data)
            #print "filereceived: " + str(filereceived)
            #print "filesize: " + str(filesize)
            with open(cmd.partition(" ")[2], 'wb') as frcvd:
                while int(filereceived)<int(filesize):
                    temp=socket_client.recv(BUFF)
                    frcvd.write(temp)
                    filereceived+=len(temp)
                frcvd.close()
        else:
            print socket_client.recv(1024)

    except socket.error, exc:
        socket_client.close()
        break