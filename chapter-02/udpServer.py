# encoding:utf-8

from socket import *
from time import ctime

HOST = ''
PORT = 12345
ADDR = (HOST, PORT)
BUFSIZE = 1024

udpServerSock = socket(AF_INET, SOCK_DGRAM)
udpServerSock.bind(ADDR)

while True:
    print("waiting for connection ...")
    data, addr = udpServerSock.recvfrom(BUFSIZE)
    data = data.decode()
    udpServerSock.sendto(('[%s] %s' % (ctime(), data)).encode(), addr)
    print("recive from and return to ", addr)
udpServerSock.close()