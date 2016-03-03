# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 12:32:48 2016

@author: sarath
"""
from verb import Verb

class Dial(Verb):
    query_params = ['number','action','method','timeout','timeLimit','record']
    variable_defaults = {'timeout': 10, 'record' : 'true', 'method':'GET'}
    name = 'dial'
    def __init__(self,variables = dict()):
        _v = Dial.variable_defaults.copy()
        _v.update(variables)
        Verb.__init__(self,Dial.name,_v)
