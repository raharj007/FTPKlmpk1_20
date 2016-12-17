import threading
import os
import pathconverter
import cwdModule
import deletehandler
import mkdModule
import modifier
import listModule

class ClientHandler(threading.Thread):
    def __init__(self, (client, address)):
        threading.Thread.__init__(self)
        self.client_socket=client
        self.address=address
        self.BUFF=1024
        self.isLogedIn=False
        self.username=""
        self.password=""
        self.CRLF="\r\n"
        self.commands=["USER","PASS","QUIT","PWD","CWD","RMD","DELE", "MKD","RNFR","RNTO"]
        self.commands=["USER","PASS","QUIT","PWD","CWD","RMD","DELE", "MKD", "LIST"]
        self.currentDirectory=os.getcwd()
        self.root= "E:\\KUNS\\KULIAH\\ProgJar\\FTPKlmpk1_20"
        self.rnfr=""
        self.rnto=""

    def run(self):
        welcome_massage="220-ProgJar Server 0.0.0 beta\r\n220-written by Cahya, Kunto, Muhsin, Panji\r\n"
        self.client_socket.sendall(welcome_massage)
        cmd="test"
        while cmd!="QUIT":
            cmd = self.client_socket.recv(self.BUFF);
            print cmd
            cmd = cmd.strip(self.CRLF);
            if cmd.upper()=="QUIT":
                print "quiting"
                self.client_socket.sendall("221 Goodbye"+self.CRLF)
                self.client_socket.close()
            elif self.isLogedIn==False:
                print "haven't login yet"
                if cmd.partition(" ")[0].upper()!="USER" and self.username=="":
                    if cmd.partition(" ")[0].upper() in self.commands:
                        self.client_socket.sendall("530 Please log in with USER and PASS first" + self.CRLF)
                    else:
                        self.sendSyntaxError()
                elif cmd.partition(" ")[0].upper()=="USER":
                    self.username=cmd.partition(" ")[2].strip()
                    print "authenticating user with username :", self.username
                    self.client_socket.sendall("331 Password required for " + self.username + self.CRLF)
                elif cmd.partition(" ")[0].upper()=="PASS":
                    print "menerima password"
                    self.password = cmd.partition(" ")[2].strip();
                    if self.password == "admin" and self.username == "admin":
                        self.client_socket.sendall("230 Logged on" + self.CRLF)
                        self.isLogedIn = True
                    else:
                        self.client_socket.sendall("530 Login or password incorrect" + self.CRLF)
                else:
                    if cmd.partition(" ")[0].upper() in self.commands:
                        print "masuk sini"
                        self.client_socket.sendall("530 Please log in with USER and PASS first" + self.CRLF)
                    else:
                        self.sendSyntaxError()
            else:
                print "masuk sini"
                command=cmd.partition(" ")[0].upper()
                print "user give command: ", command
                if command in self.commands:
                    if command=="PWD":
                        if(self.currentDirectory==self.root):
                            currentDirectory="\\"
                        else:
                            currentDirectory=pathconverter.pathconvert(self.root,self.currentDirectory)
                        self.client_socket.sendall("257 %s is current working directory\r\n"%(currentDirectory))
                    elif command=="CWD":
                        dirname=cmd.partition(" ")[2].strip()
                        self.currentDirectory=cwdModule.cwd(self.client_socket, self.root, self.currentDirectory, dirname)
                    elif command=="DELE":
                        filename=cmd.partition(" ")[2].strip()
                        deletehandler.deletefile(filename, self.client_socket, self.currentDirectory)
                    elif command=="RMD":
                        dirname=cmd.partition(" ")[2].strip()
                        deletehandler.deletefolder(dirname, self.client_socket, self.currentDirectory)
                    elif command=="MKD":
                        dirname=cmd.partition(" ")[2].strip()
                        mkdModule.mkd(self.client_socket, self.root, self.currentDirectory, dirname)
                    elif command=="RNFR":
                        path=cmd.partition(" ")[2].strip()
                        self.rnfr=modifier.rnfr(self.client_socket, self.currentDirectory, path)
                        print self.rnfr
                    elif command=="RNTO":
                        path = cmd.partition(" ")[2].strip()
                        if self.rnfr!="":
                            self.rnto=modifier.rnto(self.client_socket, self.currentDirectory, self.rnfr, path)
                            print self.rnto
                        else:
                            self.client_socket.sendall("503 Bad sequence of commands"+self.CRLF)
                    elif command=="LIST":
                        pathname=cmd.partition(" ")[2].strip()
                        if pathname=="":
                            listModule.listNoPath(self.client_socket, self.currentDirectory)
                        else:
                            listModule.list(self.client_socket, self.root, self.currentDirectory, pathname)
                else:
                    self.sendSyntaxError()


    def auth(self):
        while True:
            cmd = self.client_socket.recv(self.BUFF)
            if cmd.partition(" ")[0].upper()=="PASS":
                self.password=cmd.partition(" ")[2].strip();
                if self.password=="admin" and self.username=="admin":
                    self.client_socket.sendall("230 Logged on"+self.CRLF)
                    self.isLogedIn=True
                    break
                else:
                    self.client_socket.sendall("530 Login or password incorrect" + self.CRLF)
            else:
                if cmd.partition(" ")[0].upper() in self.commands:
                    self.client_socket.sendall("530 Please log in with USER and PASS first" + self.CRLF)
                else:
                    self.sendSyntaxError()

    def sendSyntaxError(self):
        self.client_socket.sendall("500 Syntax error, command unrecognized" + self.CRLF)