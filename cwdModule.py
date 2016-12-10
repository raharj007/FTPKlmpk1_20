import os
import pathconverter

def cwd(client_socket, root, path):
    print 'module cwd'
    currentWD = os.getcwd()
    currentPath = currentWD + "\\"
    os.chdir(currentPath + path)
    updateCurrentPath = os.getcwd()
    updateCurrentPath = pathconverter.pathconvert(root, updateCurrentPath)
    client_socket.sendall("257 %s is current working directory" % (updateCurrentPath))