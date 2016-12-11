import os

CRLF="\r\n"

def deletefile(path, client_socket, currentdirectory):
    print "currentworkingdirectory: ", currentdirectory
    print "path: ", path
    path = os.path.join(currentdirectory, path)
    print "finalpath: ", path
    if os.path.isfile(path):
        os.remove(path)
        client_socket.sendall("250 File deleted sucessfully"+CRLF)
    else:
        client_socket.sendall("550 File not found" + CRLF);

def deletefolder(path, client_socket, currentdirectory):
    print "currentworkingdirectory: ", currentdirectory
    print "path: ", path
    path=os.path.join(currentdirectory,path)
    print "finalpath: ", path
    if os.path.isdir(path):
        if not os.listdir(path):
            os.rmdir(path)
            client_socket.sendall("250 Directory deleted sucessfully" + CRLF)
        else:
            client_socket.sendall("550 Directory not empty" + CRLF)
    else:
        client_socket.sendall("550 Directory not found"+CRLF);