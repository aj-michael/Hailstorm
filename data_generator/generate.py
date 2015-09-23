import time
import uuid

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
    line = "Ride dropoff\t{!s}\t{!s}\n".format(timestamp, ride_id)

def random_lat_and_lon():
    return 4, 5
