# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 12:56:19 2016

@author: sarath
"""
from flask import  request, Response
import flask_restful
from dial import Dial
from play import Play
from say import Say

verbs_dict = {'dial' : Dial, 'play' :Play, 'say' :Say}

api = flask_restful.Api()
class VerbHandler(flask_restful.Resource):
    @api.representation('text/plain')
    def get(self, verb):
        verb_class = verbs_dict.get(verb,Say)
        query_dict = dict(request.args.items())
        verb = verb_class(query_dict)
        return Response(verb.string(), mimetype='text/xml')

    @api.representation('text/plain')
    def post(self, verb):
        verb_class = verbs_dict.get(verb,Say)
        query_dict = dict(request.args.items())
        verb = verb_class(query_dict)
        return Response(verb.string(), mimetype='text/xml')
