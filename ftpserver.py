import socket
import select
import sys
from ClientHandler import ClientHandler

port=5000

server_address = ('10.181.1.207', port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(10)

input_socket = [server_socket]
threads=[]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])

        for sock in read_ready:
            if sock == server_socket:
                (client_socket, client_address)=server_socket.accept()
                print client_address, " connected"
                c=ClientHandler((client_socket, client_address))
                c.start()
                threads.append(c)

except KeyboardInterrupt, TypeError:
    server_socket.close()
    for c in threads:
        c.join()
    sys.exit(0)
