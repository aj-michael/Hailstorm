#!/usr/bin/python2

from generate import dropoff

import argparse
import uuid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('a'), default='/data/rides')
    parser.add_argument('--ride_id')
    args = parser.parse_args()
    dropoff(args.file, args.ride_id)
