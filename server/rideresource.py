#!/usr/bin/python2

import json

from ride import Ride

from twisted.web.resource import Resource

class RideResource(Resource):
    isLeaf = True

    def __init__(self, population):
        Resource.__init__(self)
        self.population = population

    def render_POST(self, request):
        body = json.loads(request.content.readlines()[0])
        ride_id = body['id']
        timestamp = int(body['timestamp'])
        if not ride_id in self.population.rides and body['operation'] == 'pickup':
            hail = self.population.hails[body['hail_id']]
            vehicle = self.population.vehicles[body['vehicle_id']]
            self.population.rides[ride_id] = Ride(ride_id, hail, vehicle)
        ride = self.population.rides[ride_id]
        response = { 'success': True }
        if body['operation'] == 'pickup':
            ride.start(timestamp)
        elif body['operation'] == 'dropoff':
            ride.complete(timestamp)
        else:
            response = { 'success': False, 'error': 'Unknown operation' }
        return json.dumps(response)
