#!/usr/bin/python2

import json

from hailresource import HailResource

from twisted.web.server import Site
from twisted.web.resource import Resource

class Hailstorm(Resource):
    pass

if __name__ == '__main__':
    root = Hailstorm()
    root.putChild('hails', HailResource())
    #root.putChild('vehicles', VehicleResource)
    #root.putChild('rides', RideResource)
    from twisted.internet import reactor
    reactor.listenTCP(12347, Site(root))
    print "Starting hailstorm server on port 12347"
    reactor.run()
