import os
import socket
import select
import sys

CRLF="\r\n"
BUFF=1024

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect(('127.0.0.1', 5000))

#commands = ['USER raharjo\r\n', 'PASS 123\r\n', 'PWD\r\n', 'QUIT\r\n']

read_ready, write_ready, erro=select.select([socket_client],[],[],1)

for sock in read_ready:
    if(sock==socket_client):
        data=sock.recv(1024)
        print data

while True:
    try:
        cmd=raw_input()
        if cmd.partition(" ")[0].upper()=="RETR":
            socket_client.sendall(cmd+'\r\n')
            temp=socket_client.recv(BUFF)
            if temp==" ":
                print "550 File not found"
            else:
                filesize=0
                filereceived=0
                data=""
                filesize, delimiter, body=temp.partition("\r\n\r\n")
                filedownload=cmd.partition(" ")[2]
                with open(filedownload, 'wb') as frcvd:
                    data=data+body
                    filereceived=len(data)
                    frcvd.write(data)
                    while int(filereceived)<int(filesize):
                        temp=socket_client.recv(BUFF)
                        frcvd.write(temp)
                        filereceived+=len(temp)
                    frcvd.close()
                print str(filedownload) + " downloaded."
        elif cmd.partition(" ")[0].upper()=="STOR":
            filename = cmd.partition(" ")[2]
            if os.path.exists(filename):
                fileupload_size=os.path.getsize(filename)
                with open(filename,"rb") as fileupload:
                    dataupload = fileupload.read()
                    socket_client.sendall(cmd + " " + str(fileupload_size) + " " + "\r\n\r\n" + dataupload)
                print str(filename) + " uploaded."
            else:
                print "550 File not found"
        else:
            socket_client.sendall(cmd+"\r\n")
            print socket_client.recv(1024).rstrip(CRLF)
    except socket.error, exc:
        socket_client.close()
        break