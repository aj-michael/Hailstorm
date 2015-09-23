from time import time

from twisted.python import log

class Session(object):
    """A period of time that a Vehicle is online."""
    def __init__(self, start_timestamp):
        self.start_timestamp = start_timestamp
        self.rides = []
        self.in_progress = True
        self.end_timestamp = None

    def end(self, end_timestamp):
        self.in_progress = False
        self.end_timestamp = end_timestamp

    def duration(self):
        if self.in_progress:
            return int(time()) - self.start_timestamp
        else:
            return end_timestamp - self.start_timestamp

    def fields(self):
        return { 'start_timestamp': self.start_timestamp,
                 'in_progress': self.in_progress,
                 'end_timestamp': self.end_timestamp,
                 'duration': self.duration(),
                 'rides': [r.fields() for r in self.rides] }

class Vehicle(object):
    """Represents a vehicle that may go on and offline. The vehicle may pick
    up passengers while it is online."""

    OFFLINE = 0
    AVAILABLE = 1
    TRANSIT = 2

    def __init__(self, vehicle_id):
        log.msg('A vehicle was created with id {!s}.'.format(vehicle_id))
        self.vehicle_id = vehicle_id
        self.sessions = []
        self.status = Vehicle.OFFLINE

    def all_rides(self):
        [ride for ride in session.rides for session in self.sessions]

    def new_session(self, start_timestamp):
        self.sessions.append(Session(start_timestamp))
        self.status = Vehicle.AVAILABLE

    def end_session(self, end_timestamp):
        if len(self.sessions) > 0:
            self.sessions[-1].end(end_timestamp)
            self.status = Vehicle.OFFLINE

    def online(self):
        return not self.status == Vehicle.OFFLINE

    def pickup(self, ride):
        if len(self.sessions) > 0:
            self.sessions[-1].rides += [ride]
            self.status = Vehicle.TRANSIT

    def dropoff(self):
        self.status = AVAILABLE

    def available(self):
        return self.status == Vehicle.AVAILABLE

    def fields(self):
        return { 'id': self.vehicle_id,
                 'available': self.available(),
                 'online': self.online(),
                 'sessions': [s.fields() for s in self.sessions] }
