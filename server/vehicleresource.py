import json

from vehicle import Vehicle

from twisted.web.resource import Resource

class VehicleResource(Resource):
    isLeaf = True

    def __init__(self, population):
        self.population = population

    def render_POST(self, request):
        body = json.loads(request.content.readlines()[0])
        vehicle_id = body['id']
        timestamp = int(body['timestamp'])
        print "My vehicle_id is " + str(vehicle_id)
        if not vehicle_id in self.population.vehicles:
            self.population.vehicles[vehicle_id] = Vehicle(vehicle_id)
        self.population.vehicles[vehicle_id].new_session(timestamp)
        response = { 'success': True }
        return json.dumps(response)
