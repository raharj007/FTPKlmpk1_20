import os
import pathconverter

def help(socket_client, currentDirectory,path):
    print 'ini bantuan'
    bantuan = "214-The following commands are recognized:\r\n" \
              "USER   PASS   QUIT   PWD\r\nCWD   RMD   DELE   MKD\r\nRNFR   STOR   LIST   RETR\r\n214-Have a nice day."
    socket_client.sendall(bantuan)
