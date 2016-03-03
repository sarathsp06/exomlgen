# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 12:33:23 2016

@author: sarath
"""
import pystache
import os
DIR = os.path.dirname(os.path.abspath(__file__))
class Verb(object):
    def __init__(self,verb_name,variables_dict = dict()):
        self.verb = verb_name
        self.variables = variables_dict
    
    def string(self):
        f  = open(os.path.join(DIR, 'templates', self.verb)+".xml").read()
        print os.path.join(DIR, 'templates', self.verb)
        s = pystache.render(f,self.variables)
        return s