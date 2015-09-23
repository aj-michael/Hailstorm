#!/usr/bin/python2

import json

from hail import Hail

from twisted.web.resource import Resource

class HailResource(Resource):
    isLeaf = True

    def __init__(self, population):
        self.population = population

    def render_POST(self, request):
        body = json.loads(request.content.readlines()[0])
        hail_id = body['id']
        timestamp = int(body['timestamp'])
        print body.keys()
        if body['operation'] == 'hail':
            latitude = float(body['latitude'])
            longitude = float(body['longitude'])
            self.population.hails[hail_id] = Hail(
                hail_id, timestamp, latitude, longitude)
        elif body['operation'] == 'cancel':
            self.population.hails[hail_id].cancel(timestamp)
        response = { 'success': True }
        return json.dumps(response)
