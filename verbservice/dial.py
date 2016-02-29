# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 12:32:48 2016

@author: sarath
"""
from verb import Verb

class Dial(Verb):
    query_params = ['number']
    variable_defaults = dict()
    name = 'dial'
    def __init__(self,variables = dict()):
        _variables = Dial.variable_defaults.copy()
        _variables.update(variables)
        Verb.__init__(self,Dial.name,_variables)
