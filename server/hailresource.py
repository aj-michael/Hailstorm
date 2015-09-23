import json

from hail import Hail

from twisted.web.resource import Resource

class HailResource(Resource):
    def __init__(self, population):
        Resource.__init__(self)
        self.population = population

    def render_GET(self, request):
        hails = self.population.hails.values()
        return json.dumps([h.fields() for h in hails])

    def render_POST(self, request):
        body = json.loads(request.content.readlines()[0])
        hail_id = body['id']
        timestamp = int(body['timestamp'])
        response = { 'success': True }
        if body['operation'] == 'hail':
            latitude = float(body['latitude'])
            longitude = float(body['longitude'])
            self.population.hails[hail_id] = Hail(
                hail_id, timestamp, latitude, longitude)
        elif body['operation'] == 'cancel':
            self.population.hails[hail_id].cancel(timestamp)
        else:
            response = { 'success': False, 'error': 'Unknown operation' }
        return json.dumps(response)
