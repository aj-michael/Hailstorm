from time import time

class Session(object):
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
            return int(time()) - start_timestamp
        else:
            return end_timestamp - start_timestamp

class Vehicle(object):
    def __init__(self, vehicle_id):
        print "A vehicle object was just created with:"
        print vehicle_id
        self.vehicle_id = vehicle_id
        self.sessions = []

    def all_rides(self):
        [ride for ride in session.rides for session in self.sessions]

    def new_session(self, start_timestamp):
        self.sessions.append(Session(start_timestamp))

    def end_session(self, end_timestamp):
        if len(self.sessions) > 0:
            self.sessions[-1].end(end_timestamp)
