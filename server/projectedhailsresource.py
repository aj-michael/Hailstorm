import json
import time

from twisted.web.resource import Resource

class ProjectedHailsResource(Resource):
    """I estimate the number of hails in the next hour as the number of hails
    in this hour yesterday."""

    def __init__(self, population):
        Resource.__init__(self)
        self.population = population

    def render_GET(self, request):
        start = time.time() - 24 * 60 * 60
        end = start + 1 * 60 *60
        hails = self.population.hails.values()
        tally = [1 for h in hails if start < h.hail_time < end]
        return json.dumps({ 'num hails': len(tally) })
