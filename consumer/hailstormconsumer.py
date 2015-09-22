#!/usr/bin/python2

import argparse
import sys

from dataconsumer import DataConsumerFactory
from databodyproducer import HailBodyProducer, VehicleBodyProducer, RideBodyProducer

from twisted.internet.defer import succeed
from twisted.internet.protocol import ClientFactory, Protocol
from twisted.internet.task import LoopingCall
from twisted.python import filepath
from twisted.python import log
from twisted.web.client import Agent
from twisted.web.client import HTTPClientFactory
from twisted.web.http import HTTPClient
from twisted.web.http_headers import Headers
from twisted.web.iweb import IBodyProducer

from zope.interface import implements

def parse_args():
    description = """Hailstorm Data Consumer
I read taxi hailing data from the file that you specify."""
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "HAILS", type=argparse.FileType('r'),
        help="Path to the hails data source file.")
    parser.add_argument(
        "VEHICLES", type=argparse.FileType('r'),
        help="Path to the vehicles data source file.")
    parser.add_argument(
        "RIDES", type=argparse.FileType('r'),
        help="Path to the rides data source file.")
    parser.add_argument("HOST", help="Host to send data to.")
    parser.add_argument("PORT", help="Port to send data to.")
    parser.add_argument(
        "-l", "--log", help="Log file, defaults to stdout.",
        type=argparse.FileType('w'), default=sys.stdout)
    return parser.parse_args()

def consume(filepath, uri, host, port, data_body_producer):
    """I set up a file to be watched and communicated to a uri via HTTP."""
    factory = DataConsumerFactory(filepath, uri, data_body_producer)
    from twisted.internet import reactor
    reactor.connectTCP(host, int(port), factory)
    log.msg('Consuming data from {!s} and alerting {!s}.'.format(filepath, uri))

if __name__ == '__main__':
    args = parse_args()
    log.startLogging(args.log)
    uri = 'http://{!s}:{!s}/{{!s}}'.format(args.HOST, args.PORT)
    consume(
        args.HAILS, uri.format('hails'), args.HOST, args.PORT, HailBodyProducer)
    consume(
        args.VEHICLES, uri.format('vehicles'), args.HOST, args.PORT,
        VehicleBodyProducer)
    consume(
        args.RIDES, uri.format('rides'), args.HOST, args.PORT, RideBodyProducer)
    from twisted.internet import reactor
    reactor.run()
