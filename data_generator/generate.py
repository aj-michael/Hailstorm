#!/usr/bin/python2

import argparse
import time
import uuid

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hails_path', type=argparse.FileType('a'), default='/data/hails')
    return parser.parse_args()

def new_hail(file_obj): 
    hail_id = uuid.uuid1()
    timestamp = int(time.time())
    latitude, longitude = random_lat_and_lon()
    line = "New hail"
    line += '\t'
    line += str(timestamp)
    line += '\t'
    line += str(hail_id)
    line += '\t'
    line += str(latitude)
    line += '\t'
    line += str(longitude)
    line += '\n'
    file_obj.write(line)

def new_vehicle(file_obj): 
    vehicle_id = uuid.uuid1()
    timestamp = int(time.time())
    latitude, longitude = random_lat_and_lon()
    line = "New vehicle"
    line += '\t'
    line += str(timestamp)
    line += '\t'
    line += str(vehicle_id)
    line += '\n'
    file_obj.write(line)

def new_ride(file_obj): 
    vehicle_id = uuid.uuid1()
    timestamp = int(time.time())
    latitude, longitude = random_lat_and_lon()
    line = "New hail"
    line += '\t'
    line += str(timestamp)
    line += '\t'
    line += str(hail_id)
    line += '\n'
    file_obj.write(line)

def random_lat_and_lon():
    return 4, 5

if __name__ == '__main__':
    args = parse_args()
    new_hail(args.hails_path)
