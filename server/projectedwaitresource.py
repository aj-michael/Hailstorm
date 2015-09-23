import json
import time

from twisted.web.resource import Resource

class ProjectedWaitResource(Resource):
    """I estimate the average wait time over the next hour by calculating the
    average waittime over this hour yesterday."""

    def __init__(self, population):
        Resource.__init__(self)
        self.population = population

    def render_GET(self, request):
        start = time.time() - 24 * 60 * 60
        end = start + 1 * 60 *60
        hails = self.population.hails.values()
        times = [h.waittime() for h in hails if start < h.hail_time < end]
        if len(times) == 0:
            response = { 'error': 'INSUFFICIENT DATA FOR MEANINGFUL ANSWER' }
        else:
            response = { 'wait mins': sum(times) / float(len(times)) / 60.0 }
        return json.dumps(response)
