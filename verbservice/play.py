# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:15:18 2016

@author: sarath
"""
from verb import Verb

class Play(Verb):
    query_params = ['loop','digits','url']
    variable_defaults = {'loop' : 0}
    name = 'play'
    def __init__(self,variables = dict()):
        _v = Play.variable_defaults.copy()
        _v.update(variables)
        Verb.__init__(self,Play.name,_v)