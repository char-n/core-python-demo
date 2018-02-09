# encoding=utf-8

from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 12345
ADDR = (HOST, PORT)

# 继承的用法
# readline()之后需要decode()方法。还是跟普通的tcp一样。接收到的信息需要解码，发送的信息需要编码
class MyRequestHandler(SRH):
    def handle(self):
        print('connect from ', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline().decode())).encode())


tcp = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcp.serve_forever()
