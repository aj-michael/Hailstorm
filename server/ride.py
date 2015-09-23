from time import time

class Ride(object):
    def __init__(ride_id, hail_id, vehicle_id):
        self.ride_id = ride_id
        self.hail_id = hail_id
        self.vehicle_id = vehicle_id
        self.start_timestamp = None
        self.end_timestamp = None
        self.in_progress = True

    def start(start_timestamp):
        self.start_timestamp = start_timestamp
        self.in_progress = True

    def complete(end_timestamp):
        self.end_timestamp = end_timestamp
        self.in_progress = False

    def duration():
        if self.in_progress:
            return int(time()) - self.start_timestamp
        else:
            return self.end_timestamp - self.start_timestamp
