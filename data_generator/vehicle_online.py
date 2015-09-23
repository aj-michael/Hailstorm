#!/usr/bin/python2

from generate import vehicle_online

import argparse
import uuid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('a'), default='/data/vehicles')
    parser.add_argument('--vehicle_id', default=uuid.uuid1())
    args = parser.parse_args()
    vehicle_online(args.file, args.vehicle_id)
