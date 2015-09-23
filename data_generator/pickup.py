#!/usr/bin/python2

from generate import pickup

import argparse
import uuid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('a'), default='/data/rides')
    parser.add_argument('--hail_id')
    parser.add_argument('--vehicle_id')
    parser.add_argument('--ride_id')
    args = parser.parse_args()
    pickup(args.file, args.hail_id, args.vehicle_id, args.ride_id)
