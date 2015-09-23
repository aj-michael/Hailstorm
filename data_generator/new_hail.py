#!/usr/bin/python2

from generate import new_hail

import argparse
import uuid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('a'), default='/data/hails')
    parser.add_argument('--hail_id', default=uuid.uuid1())
    args = parser.parse_args()
    new_hail(args.file, args.hail_id)
