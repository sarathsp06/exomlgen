# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:08:28 2016

@author: sarath
"""
from verb import Verb

class Say(Verb):
    query_params = ['loop','text','voice','language']
    variable_defaults = {'language' : 'en', 'loop': 1, 'voice' : 'man'}
    name = 'say'
    def __init__(self,variables = dict()):
        _v = Say.variable_defaults.copy()
        _v.update(variables)
        Verb.__init__(self,Say.name,_v)