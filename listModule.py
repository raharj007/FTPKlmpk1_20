import os
import pathconverter

def list(client_socket, root, currentDir, pathName):
    print 'list normal'
    nameDir = ''
    joinPath = os.path.join(currentDir, pathName)
    if os.path.exists(joinPath):
        updateCurrentPath = pathconverter.pathconvert(root, joinPath)
        if os.path.isdir(joinPath):
            if not os.listdir(joinPath):
                client_socket.sendall('\r\n')
            else:
                directoryList = os.listdir(joinPath)
                for directory in directoryList:
                    nameDir = nameDir + updateCurrentPath + '\\' + directory + '\r\n'
                client_socket.sendall(nameDir)
        else:
            if os.path.isfile(joinPath):
                client_socket.sendall('%s\r\n' % (updateCurrentPath))
            else:
                client_socket.sendall('\r\n')

def listNoPath(client_socket, currentDir):
    print 'list tanpa path'
    nameDir = ''
    if not os.listdir(currentDir):
        client_socket.sendall('\r\n')
    else:
        directoryList = os.listdir(currentDir)
        for directory in directoryList:
            nameDir = nameDir + directory + '\r\n'
        client_socket.sendall(nameDir)

