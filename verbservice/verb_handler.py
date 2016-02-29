# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 12:56:19 2016

@author: sarath
"""
from flask import  request, Response
import flask_restful
from dial import Dial


verbs_dict = {'dial' : Dial}

api = flask_restful.Api()
class VerbHandler(flask_restful.Resource):
    @api.representation('text/plain')
    def get(self, verb):
        verb_class = verbs_dict.get(verb,Dial)
        query_dict = dict((param, request.args.get(param)) for param in verb_class.query_params)
        verb = verb_class(query_dict)
        return Response(verb.string(), mimetype='text/xml')

    @api.representation('text/plain')
    def post(self, verb):
        verb_class = verbs_dict.get(verb,Dial)
        query_dict = dict((param, request.args.get(param)) for param in Dial.query_params)
        verb = verb_class(query_dict)
        return Response(verb.string(), mimetype='text/xml')
