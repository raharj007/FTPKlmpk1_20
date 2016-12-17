import os
import pathconverter

def cwd(client_socket, root, currentWD, path):
    print 'module cwd'
    print path
    joinPath = os.path.join(currentWD, path)
    if(os.path.isdir(joinPath) and os.path.exists(joinPath)):
        updateCurrentPath = pathconverter.pathconvert(root, joinPath)
        client_socket.sendall('250 CWD successfull. "%s" is current working directory\r\n' % (updateCurrentPath))
        return joinPath
    else:
        client_socket.sendall('550 CWD failed. "%s": directory not found.\r\n' % joinPath)
        return currentWD