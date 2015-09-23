import time

from twisted.python import log

class Hail(object):
    """I represent a requested taxi. I may be waiting, cancelled or dropped
    off."""
    
    # Enums weren't introduced until 3.4 and I don't want to force a dependency
    # on PyPi.
    WAITING = 0
    TRANSIT = 1
    ARRIVED = 2
    CANCELLED = 3

    def __init__(self, hail_id, timestamp, latitude, longitude):
        log.msg('A hail was created with id {!s}.'.format(hail_id))
        self.hail_id = hail_id

        self.latitude = latitude
        self.longitude = longitude

        self.status = Hail.WAITING

        self.hail_time = timestamp
        self.pickup_time = None
        self.dropoff_time = None
        self.cancel_time = None

    def pickup(self, timestamp):
        self.status = Hail.TRANSIT
        self.pickup_time = timestamp

    def dropoff(self, timestamp):
        self.status = Hail.ARRIVED
        self.dropoff_time = timestamp

    def cancel(self, timestamp):
        self.status = Hail.CANCELLED
        self.cancel_time = timestamp

    def waittime(self):
        if self.pickup_time == None:
            return int(time.time()) - self.hail_time
        else:
            return self.pickup_time - self.hail_time

    def fields(self):
        """Queryable fields that can be sent back to the user. None fields are
        excluded."""
        fields = { 'id': self.hail_id,
                   'hail_time': self.hail_time,
                   'location': { 'latitude': self.latitude,
                                 'longitude': self.longitude },
                   'pickup_time': self.pickup_time,
                   'dropoff_time': self.dropoff_time,
                   'cancel_time': self.cancel_time }
        return { k: v for k, v in fields.items() if v }
