from twisted.internet.protocol import ClientFactory, Protocol, connectionDone
from twisted.internet.task import LoopingCall
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

def check_file(file_obj, callback):
    """If there is a line of fileObj that has not been read yet, I'll call you
    back with it."""
    line = file_obj.readline()
    if line:
        callback(line)

class DataConsumerProtocol(Protocol):
    """I watch for file appends, transform them into an HTTP request and send
    them to a URL."""

    def connectionMade(self):
        self.loop = LoopingCall(check_file, self.factory.sourcefile, self.consume)
        self.loop.start(0.1)

    def consume(self, line):
        from twisted.internet import reactor
        Agent(reactor).request(
            'POST', self.factory.url,
            Headers({'User-Agent': ['Hailstorm data source']}),
            self.factory.data_body_producer(line))

    def connectionLost(self, reason=connectionDone):
        self.loop.stop()

class DataConsumerFactory(ClientFactory):
    """I build instances of DataConsumerProtocol for a specific data source
    file, url, and data to request body transformation."""

    protocol = DataConsumerProtocol

    def __init__(self, sourcefile, url, data_body_producer):
        self.sourcefile = sourcefile
        self.url = url
        self.data_body_producer = data_body_producer
