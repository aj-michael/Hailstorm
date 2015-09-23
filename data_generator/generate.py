#!/usr/bin/python2

import argparse
import time
import uuid

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hails_path', type=argparse.FileType('a'), default='/data/hails')
    parser.add_argument('--vehicles_path', type=argparse.FileType('a'), default='/data/vehicles')
    parser.add_argument('--rides_path', type=argparse.FileType('a'), default='/data/rides')
    return parser.parse_args()

def new_hail(file_obj, hail_id=uuid.uuid1()): 
    timestamp = int(time.time())
    latitude, longitude = random_lat_and_lon()
    line = "New hail\t{!s}\t{!s}\t{!s}\t{!s}\n".format(
        timestamp, hail_id, latitude, longitude)
    file_obj.write(line)

def cancel_hail(file_obj, hail_id): 
    timestamp = int(time.time())
    line = "Cancelled hail\t{!s}\t{!s}\n".format(timestamp, hail_id)
    file_obj.write(line)

def vehicle_online(file_obj, vehicle_id=uuid.uuid1()): 
    vehicle_id = uuid.uuid1()
    timestamp = int(time.time())
    line = "Vehicle online\t{!s}\t{!s}\n".format(timestamp, vehicle_id)
    file_obj.write(line)

def vehicle_offline(file_obj, vehicle_id): 
    timestamp = int(time.time())
    line = "Vehicle offline\t{!s}\t{!s}\n".format(timestamp, vehicle_id)
    file_obj.write(line)

def pickup(file_obj, hail_id, vehicle_id, ride_id=uuid.uuid1()): 
    timestamp = int(time.time())
    line = "Ride pickup\t{!s}\t{!s}\t{!s}\t{!s}\n".format(
        timestamp, ride_id, hail_id, vehicle_id)
    file_obj.write(line)

def dropoff(file_obj, ride_id):
    timestamp = int(time.time())
    line = "Ride pickup\t{!s}\t{!s}\t{!s}\t{!s}\n".format(timestamp, ride_id)

def random_lat_and_lon():
    return 4, 5

if __name__ == '__main__':
    args = parse_args()
    new_hail(args.hails_path)
    new_vehicle(args.vehicles_path)
    #new_ride(args.rides_path)
