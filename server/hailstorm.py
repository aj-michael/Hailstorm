#!/usr/bin/python2

import argparse
import json
import sys

from hail import Hail
from population import Population
from vehicle import Vehicle

from hailresource import HailResource
from rideresource import RideResource
from vehicleresource import VehicleResource

from hailmetricsresource import HailMetricsResource
from vehiclemetricsresource import VehicleMetricsResource

from pasthourhailsresource import PastHourHailsResource
from projectedhailsresource import ProjectedHailsResource
from projectedwaitresource import ProjectedWaitResource

from twisted.python import log
from twisted.web.server import Site
from twisted.web.resource import Resource

def parse_args():
    description = """Hailstorm Backend Server
I store hail data and provide an HTTP API."""
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--port', help="Port to listen on.", default=12347)
    parser.add_argument(
        '--log', help='Log file, defaults to stdout.',
        type=argparse.FileType('w'), default=sys.stdout)
    return parser.parse_args()

class Hailstorm(Resource):
    pass

class Status(Resource):
    pass

def main():
    """Sets up the structure of the HTTP API in terms of resources as nodes in
    a tree. Then starts the server."""
    args = parse_args()
    log.startLogging(args.log)
    population = Population()
    root = Hailstorm()
    hails = HailResource(population)
    vehicles = VehicleResource(population)
    rides = RideResource(population)
    status = Status()
    root.putChild('hails', hails)
    root.putChild('rides', rides)
    root.putChild('status', status)
    root.putChild('vehicles', vehicles)
    hails.putChild('waiting', HailMetricsResource(population, Hail.WAITING))
    hails.putChild('transit', HailMetricsResource(population, Hail.TRANSIT))
    hails.putChild('arrived', HailMetricsResource(population, Hail.ARRIVED))
    hails.putChild('cancelled', HailMetricsResource(population, Hail.CANCELLED))
    vehicles.putChild(
        'offline', VehicleMetricsResource(population, Vehicle.OFFLINE))
    vehicles.putChild(
        'available', VehicleMetricsResource(population, Vehicle.AVAILABLE))
    vehicles.putChild(
        'transit', VehicleMetricsResource(population, Vehicle.TRANSIT))
    status.putChild('projectedhails', ProjectedHailsResource(population))
    status.putChild('projectedwait', ProjectedWaitResource(population))
    status.putChild('pasthourhails', PastHourHailsResource(population))
    from twisted.internet import reactor    
    reactor.listenTCP(int(args.port), Site(root))
    log.msg('Starting hailstorm server on port {!s}'.format(args.port))
    reactor.run()

if __name__ == '__main__':
    main()
