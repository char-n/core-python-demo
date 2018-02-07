# encoding:utf-8

from socket import *

# 创建tcp
tcpSock = socket(AF_INET, SOCK_STREAM)

# 创建udp
udpSock = socket(AF_INET, SOCK_DGRAM)
