#!/usr/bin/python2

from generate import cancel_hail

import argparse
import uuid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('a'), default='/data/vehicles')
    parser.add_argument('VEHICLE_ID')
    args = parser.parse_args()
    vehicle_offline(args.file, args.VEHICLE_ID)
