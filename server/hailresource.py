#!/usr/bin/python2

import json

from twisted.web.resource import Resource

class HailResource(Resource):
    isLeaf = True

    def __init__(self):
        self.passengers = []

    def render(self, request):
        body = json.loads(request.content.readlines()[0])
        print "Here with"
        print body
        operations = { 'POST': 'create',
                       'GET': 'read',
                       'PUT': 'update',
                       'DELETE': 'delete' }
        if request.method not in operations: 
            response = {
                'success': False,
                'error': 'InvalidRequestMethod',
                'error_message': ("Valid request methods: %s" % (', '.join(operations.keys))) }
        else:
            response = { 'success': True }
        return json.dumps(response)
