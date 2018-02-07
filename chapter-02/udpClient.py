# encoding:utf-8
from socket import *

HOST = 'localhost'
PORT = 12345
ADDR = (HOST, PORT)
BUFSIZE = 1024

udpClientSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpClientSock.sendto(data.encode(), ADDR)
    data, addr = udpClientSock.recvfrom(BUFSIZE)
    data = data.decode()
    if not data:
        break
    print(data)
udpClientSock.close()
