import json

from twisted.web.resource import Resource

class HailMetricsResource(Resource):
    def __init__(self, population, status):
        Resource.__init__(self)
        self.population = population
        self.status = status

    def render_GET(self, request):
        hails = [h for h in self.population.hails.values() if h.status == self.status]
        return json.dumps([h.fields() for h in hails])
