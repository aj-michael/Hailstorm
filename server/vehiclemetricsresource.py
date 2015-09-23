import json

from twisted.web.resource import Resource

class VehicleMetricsResource(Resource):
    def __init__(self, population, status):
        Resource.__init__(self)
        self.population = population
        self.status = status

    def render_GET(self, request):
        vehicles = self.population.vehicles.values()
        vehicles = [v for v in vehicles if v.status == self.status]
        return json.dumps([v.fields() for v in vehicles])

