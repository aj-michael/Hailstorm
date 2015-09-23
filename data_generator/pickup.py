#!/usr/bin/python2

from generate import pickup

import argparse
import uuid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('a'), default='/data/rides')
    parser.add_argument('--ride_id', default=uuid.uuid1())
    args = parser.parse_args()
    pickup(args.file, args.ride_id)
