import os
import pathconverter

def list(client_socket, root, currentDir, pathName):
    print 'list normal'
    nameDir = ''
    joinPath = os.path.join(currentDir, pathName)
    if os.path.exists(joinPath):
        updateCurrentPath = pathconverter.pathconvert(root, joinPath)
        if os.path.isdir(joinPath):
            directoryList = os.listdir(joinPath)
            for directory in directoryList:
                nameDir = nameDir + updateCurrentPath + '\\' + directory + '\r\n'
            client_socket.sendall(nameDir)
        else:
            client_socket.sendall('%s\r\n' % (updateCurrentPath))

def listNoPath(client_socket, currentDir):
    print 'list tanpa path'
    nameDir = ''
    directoryList = os.listdir(currentDir)
    for directory in directoryList:
        nameDir = nameDir + directory + '\r\n'
    client_socket.sendall(nameDir)

