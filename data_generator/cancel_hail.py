#!/usr/bin/python2

from generate import cancel_hail

import argparse
import uuid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('a'), default='/data/hails')
    parser.add_argument('HAIL_ID')
    args = parser.parse_args()
    cancel_hail(args.file, args.HAIL_ID)
