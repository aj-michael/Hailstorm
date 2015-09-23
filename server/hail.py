class Hail(object):
    """I represent a requested taxi. I may be waiting, cancelled or dropped
    off."""
    
    # Enums weren't introduced until 3.4 and I don't want to force a dependency
    # on PyPi.
    WAITING = 0
    PICKED_UP = 1
    DROPPED_OFF = 2
    CANCELLED = 3

    def __init__(self, hail_id, timestamp, latitude, longitude):
        self.hail_id = hail_id

        self.latitude = latitude
        self.longitude = longitude

        self.status = Hail.WAITING

        self.hail_time = timestamp
        self.pickup_time = None
        self.dropoff_time = None
        self.cancel_time = None

    def pickup(self, timestamp):
        self.status = Hail.PICKED_UP
        self.pickup_time = timestamp

    def dropoff(self, timestamp):
        self.status = Hail.DROPPED_OFF
        self.dropoff_time = timestamp

    def cancel(self, timestamp):
        self.status = Hail.CANCELLED
        self.cancel_time = timestamp
