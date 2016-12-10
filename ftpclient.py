import socket
import select
import sys

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
        print socket_client.recv(1024)

    except socket.error, exc:
        socket_client.close()
        break