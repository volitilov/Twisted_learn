# Эго - сервер ТСР отметок времени, в котором используются классы 
# компонента internet инфрасrруктуры Twisted.

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from twisted.internet import protocol, reactor
from time import ctime

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PORT = 21567

class TSServProtocol(protocol.Protocol):
	def connectionMade(self):
		clnt = self.clnt = self.transport.getPeer().host
		print('...connected from:', clnt)

	def dataReceived(self, data):
		agr_data = bytes('[{}] {}'.format(ctime(), 
			data), 'utf-8')
		self.transport.write(agr_data)


factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
