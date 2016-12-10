import os
import pathconverter

def cwd(client_socket, root, currentWD, path):
    print 'module cwd'
    if(os.path.isdir(path)):
        joinPath = os.path.join(currentWD, path)
        updateCurrentPath = pathconverter.pathconvert(root, joinPath)
        client_socket.sendall("257 %s is current working directory" % (updateCurrentPath))
        return updateCurrentPath
    else:
        client_socket.sendall("550 CWD failed. %s : directory not found." % os.path.join(currentWD, path))
        return currentWD