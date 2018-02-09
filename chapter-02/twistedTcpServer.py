# encoding=utf-8

from twisted.internet import reactor, protocol
from time import ctime

# Twisted是一个事件驱动的网络框架

PORT = 12345


class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('connect from', clnt)

    def dataReceived(self, data):
        print('resv data %s' % data)
        self.transport.write(('[%s] %s' % (ctime(), data.decode())).encode())


factory = protocol.Factory()
factory.protocol = TSServerProtocol
print("waiting for connection...")
reactor.listenTCP(PORT, factory)
reactor.run()
