# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:41:54 2016

@author: sarath
"""
from datastore import Datastore
from flask import  request, Response
import flask_restful

api = flask_restful.Api()
class Echo(flask_restful.Resource):
    query_params = ['digits']
    @api.representation('text/plain')
    def get(self, test, id):
        query_dict = dict((param, request.args.get(param, None)) for param in Echo.query_params)
        datastore = Datastore(test, id, query_dict.get('digits'))
        return Response(datastore.read(), mimetype='text/xml')

    @api.representation('text/plain')
    def post(self, test, id):
        query_dict = dict((param, request.args.get(param)) for param in Echo.query_params)
        datastore = Datastore(test, id,query_dict.get('digits',None))
        return Response(datastore.read(), mimetype='text/xml')

    def put(self, test, id):
        query_dict =  dict((param, request.args.get(param)) for param in Echo.query_params)
        datastore = Datastore(test, id, query_dict.get('digits',None), request.data)
        datastore.save()
        return {"status" : True}
