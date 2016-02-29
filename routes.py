# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 15:25:29 2016

@author: sarath
"""
from echoservice import Echo
from verbservice import VerbHandler as Verb

routes = {
     '/echo/<string:test>/<string:id>' : Echo ,
     '/verb/<string:verb>': Verb 
}
