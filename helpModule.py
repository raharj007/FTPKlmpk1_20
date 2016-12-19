import os
import pathconverter

def help(socket_client):
    print 'ini bantuan'
    bantuan = "214-The following commands are recognized:\r\n" \
              "  USER\tPASS\tQUIT\tPWD\r\n  CWD\tRMD\tDELE\tMKD\r\n  RNFR\tSTOR\tLIST\tRETR\r\n214-Have a nice day."
    socket_client.sendall(bantuan)
