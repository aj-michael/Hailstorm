#!/usr/bin/python2

import json

from ride import Ride

from twisted.web.resource import Resource

class RideResource(Resource):
    isLeaf = True

    def __init__(self, population):
        self.population = population

    def render_POST(self, request):
        body = json.loads(request.content.readlines()[0])
        ride_id = body['id']
        hail_id = body['hail_id']
        vehicle_id = body['vehicle_id']
        timestamp = int(body['timestamp'])
        if not ride_id in self.population.rides:
            self.population.rides[ride_id] = Ride(ride_id, hail_id, vehicle_id)
        ride = self.population.rides[ride_id]
        if body['operation'] == 'pickup':
            ride.start(timestamp)
        elif body['operation'] == 'dropoff':
            ride.complete(timestamp)
        response = { 'success': True }
        return json.dumps(response)
