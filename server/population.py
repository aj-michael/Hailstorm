class Population(object):
    """I represent an isolated ecosystem of Vehicles, Hails and Rides."""

    def __init__(self):
        self.hails = {}
        self.rides = {}
        self.vehicles = {}
