# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:47:10 2016

@author: sarath
"""
import os
from flask import Response
DIR = os.path.dirname(os.path.abspath(__file__))
def hangup(test = None, id = None):
    data = ""
    with open(os.path.join(DIR,'echoservice', 'datastore', 'hangup.xml'), 'r') as f:
        data = f.read()
    append = "\n\r<!-- \n Sending hangup as exoml is not specified  for {0}/{1}\n-->" if test  is not None else ""
    return data + append


def setroutes(api,route_dict):
    for key in route_dict:
        api.add_resource(route_dict[key],key)
    
def handle404(app,api):
    """For handling 404 exception with a hangup response
    """
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    @api.representation('text/plain')
    def notfound(path):
        return Response(hangup("",""), mimetype='text/xml')