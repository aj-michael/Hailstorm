import json
import time

from twisted.web.resource import Resource

class PastHourHailsResource(Resource):
    """I provide the number of hails in the past hour, broken down by
    category."""

    def __init__(self, population):
        Resource.__init__(self)
        self.population = population

    def render_GET(self, request):
        end = time.time()
        start = end - 1 * 60 * 60
        hails = self.population.hails.values()
        hails = [h for h in hails if start < h.hail_time < end]
        waiting = [h for h in hails if h.status == Hail.WAITING]
        transit = [h for h in hails if h.status == Hail.TRANSIT]
        arrived = [h for h in hails if h.status == Hail.ARRIVED]
        cancelled = [h for h in hails if h.status == Hail.CANCELLED]
        return json.dumps({ 'total': len(hails),
                            'waiting': len(waiting),
                            'transit': len(transit),
                            'arrived': len(arrived) })
