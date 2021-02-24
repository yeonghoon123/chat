
from twisted.internet import protocol, reactor
import names

COLORS =[
    '\033[31m',#red
    '\033[32m',#red
    '\033[33m',#red
    '\033[34m',#red
    '\033[35m',#red
    '\033[36m',#red
    '\033[37m',#red
    '\033[34m',#red
]

transports = set()
users = set()

class Chat(protocol.Protocol):
    def connectionMade(self):
        name = names.get_first_name()
        color = COLORS[len(users) % len(COLORS)]
        users.add(name)
        transports.add(self.transport)

        self.transport.write(f'{color}{name}\033[0m'.encode())

    def dataReceived(self, data):
        for t in transports:
            if self.transport is not t:
                t.write(data)
        print(data.decode('utf-8'))

class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat()

print('server started!')
reactor.listenTCP(8000, ChatFactory())
reactor.run()