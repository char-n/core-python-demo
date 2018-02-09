# encoding=utf-8

from twisted.internet import reactor, protocol

HOST = 'localhost'
PORT = 12345


class TSClientProtocol(protocol.Protocol):
    def dataReceived(self, data):
        print(data.decode())
        self.sendData()

    def connectionMade(self):
        self.sendData()

    def sendData(self):
        data = input('> ')
        if data:
            print('sending data %s' % data)
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()


class TSClientFactory(protocol.ClientFactory):
    protocol = TSClientProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSClientFactory())
reactor.run()
