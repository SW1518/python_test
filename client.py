#simple client

import socket

s = socket.socket()

#host = socket.gethostbyname(socket.gethostname())
host = socket.getfqdn()
port = 1234

s.connect((host, port))
print(s.recv(1024))