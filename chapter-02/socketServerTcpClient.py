# encoding=utf-8

from socket import *

HOST = 'localhost'
PORT = 12345
ADDR = (HOST, PORT)
BUFSIZE = 1024

while True:
    tcpCli = socket(AF_INET, SOCK_STREAM)
    tcpCli.connect(ADDR)

    data = input('> ')
    if not data:
        break
    tcpCli.send(('%s\r\n' % data).encode())
    data = tcpCli.recv(BUFSIZE).decode()
    if not data:
        break
    print(data.strip())
    tcpCli.close()
