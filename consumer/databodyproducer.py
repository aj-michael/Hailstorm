import json

from twisted.internet.defer import succeed
from twisted.web.iweb import IBodyProducer

from zope.interface import implements

class DataBodyProducer(object):
    """I transform a data source line into the body of an HTTP request.
    I work well with twisted.web.client.Agent to create requests."""

    implements(IBodyProducer)

    def __init__(self, line):
        self.body = self.parse(line)
        self.length = len(self.body)

    def startProducing(self, consumer):
        consumer.write(self.body)
        return succeed(None)

    def parse(self, line):
        return line

    def pauseProducing(self):
        pass

    def stopProducing(self):
        pass

class HailBodyProducer(DataBodyProducer):
    """I specifically parse hail data source lines.
    This includes hails and cancelled hails."""

    def parse(self, line):
        data = line.rstrip().split('\t')
        body = {}
        body['timestamp'] = data[1]
        body['id'] = data[2]
        body['latitude'] = data[3]
        body['longitude'] = data[4]
        if data == 'New hail':
            body['operation'] = 'hail'
        elif data == 'Cancelled hail':
            body['operation'] = 'cancel'
        return json.dumps(body)

class VehicleBodyProducer(DataBodyProducer):
    """I specifically parse vehicle data source lines.
    This includes vehicles coming online and going offline."""

    def parse(self, line):
        data = line.rstrip().split('\t')
        body = []
        body['timestamp'] = data[1]
        body['id'] = data[2]
        if data == 'Vehicle online':
            body['operation'] = 'online'
        elif data == 'Vehicle offline':
            body['operation'] = 'offline'
        return json.dumps(body)

class RideBodyProducer(DataBodyProducer):
    """I specifically parse ride data source lines.
    This includes pickups and dropoffs."""

    def parse(self, line):
        data = line.rstrip().split('\t')
        body = []
        body['timestamp'] = data[1]
        body['passenger_id'] = data[2]
        body['vehicle_id'] = data[3]
        if data == 'Pickup':
            body['operation'] = 'pickup'
        elif data == 'Drop off':
            body['operation'] = 'dropoff'
        return json.dumps(body)
