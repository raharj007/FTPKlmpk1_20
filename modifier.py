import os

CRLF="\r\n"

def rnfr(client_socket, currentdirectory, path):
    path=os.path.join(currentdirectory, path)
    if os.path.isfile(path):
        client_socket.sendall("350 File exists, ready for destination name"+CRLF)
        return path
    elif os.path.isdir(path):
        client_socket.sendall("350 Directory exists, ready for destination name"+CRLF)
        return path
    else:
        return ""

def rnto(client_socket, currentdirectory, rnfr, path):
    path=os.path.join(currentdirectory, path)
    print "renaming from %s to %s"%(rnfr,path)
    os.rename(rnfr, path)
    client_socket.sendall("250 File renamed sucessfully"+CRLF)
    return path