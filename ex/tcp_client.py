#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from twisted.internet import protocol, reactor

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
	def sendData(self):
		data = input('> ')
		if data:
			print('...sending {}'.format(data))
			self.transport.write(bytes(data, 'utf-8'))
		else:
			self.transport.loseConnection()

	def connectionMade(self):
		self.sendData()

	def dataReceived(self, data):
		print(data.decode('utf-8'))
		self.sendData()


class TSClntFactory(protocol.ClientFactory):
	protocol = TSClntProtocol
	client_connection_lost = client_connection_failed = \
		lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()