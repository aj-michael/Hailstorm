#!/usr/bin/python2

import json

from hailresource import HailResource
from vehicleresource import VehicleResource
from rideresource import RideResource
from population import Population

from twisted.web.server import Site
from twisted.web.resource import Resource

class Hailstorm(Resource):
    pass

if __name__ == '__main__':
    root = Hailstorm()
    population = Population()
    root.putChild('hails', HailResource(population))
    root.putChild('vehicles', VehicleResource(population))
    root.putChild('rides', RideResource(population))
    from twisted.internet import reactor    
    reactor.listenTCP(12347, Site(root))
    print "Starting hailstorm server on port 12347"
    reactor.run()
