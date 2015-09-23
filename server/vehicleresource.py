import json

from vehicle import Vehicle

from twisted.web.resource import Resource

class VehicleResource(Resource):
    def __init__(self, population):
        Resource.__init__(self)
        self.population = population

    def render_GET(self, request):
        vehicles = self.population.vehicles.values()
        return json.dumps([v.fields() for v in vehicles])

    def render_POST(self, request):
        body = json.loads(request.content.readlines()[0])
        vehicle_id = body['id']
        timestamp = int(body['timestamp'])
        if not vehicle_id in self.population.vehicles:
            self.population.vehicles[vehicle_id] = Vehicle(vehicle_id)
        vehicle = self.population.vehicles[vehicle_id]
        response = { 'success': True }
        if body['operation'] == 'online':
            vehicle.new_session(timestamp)
        elif body['operation'] == 'offline':
            vehicle.end_session(timestamp)
        else:
            response = { 'success': False, 'error': 'Unknown operation' }
        return json.dumps(response)
