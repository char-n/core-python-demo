# encoding:utf-8

from socket import *
from time import ctime


'''
书上的例子有问提，执行的时候报错
参考 http://blog.csdn.net/yexiaohhjk/article/details/68066843 改为下面的形式
'''
HOST = ''
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpServerSock = socket(AF_INET, SOCK_STREAM)
tcpServerSock.bind(ADDR)
tcpServerSock.listen(5)

while True:
    print('waiting for connection ...')
    tcpCliSock, addr = tcpServerSock.accept()
    print('connect from ', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZE).decode()
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())
    tcpCliSock.close()
tcpServerSock.close()
