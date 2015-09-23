import logging
from time import time

from twisted.python import log

logger = logging.getLogger(__name__)

class Ride(object):
    def __init__(self, ride_id, hail, vehicle):
        msg = 'A Ride object was created for hail {!s} and vehicle {!s}.'
        log.msg(msg.format(hail.hail_id, vehicle.vehicle_id))
        self.ride_id = ride_id
        self.hail = hail
        self.vehicle = vehicle
        self.start_timestamp = None
        self.end_timestamp = None
        self.in_progress = True

    def start(self, start_timestamp):
        self.start_timestamp = start_timestamp
        self.in_progress = True
        self.hail.pickup(start_timestamp)
        self.vehicle.pickup(self)

    def complete(self, end_timestamp):
        self.end_timestamp = end_timestamp
        self.in_progress = False
        self.hail.dropoff(end_timestamp)

    def duration(self):
        if self.in_progress:
            return int(time()) - self.start_timestamp
        else:
            return self.end_timestamp - self.start_timestamp

    def fields(self):
        return { 'ride_id': self.ride_id,
                 'hail_id': self.hail.hail_id,
                 'vehicle_id': self.vehicle.vehicle_id,
                 'start_timestamp': self.start_timestamp,
                 'end_timestamp': self.end_timestamp,
                 'in_progress': self.in_progress,
                 'duration': self.duration() }
