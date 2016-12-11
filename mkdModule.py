import os
import pathconverter

def mkd(client_socket, root, currentWD, directoryName):
    print 'module mkd'
    if not (os.path.exists(directoryName)):
        joinPath = os.path.join(currentWD, directoryName)
        updateCurrentPath = pathconverter.pathconvert(root, joinPath)
        os.makedirs(joinPath)
        client_socket.sendall('257 "%s" created successfully\r\n' % (updateCurrentPath))
    else:
        client_socket.sendall("550 Directory already exist\r\n")
