# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:58:35 2016

@author: sarath
"""
from flask import Flask
from config import host_ip,host_port,debug
import flask_restful
from utils import setroutes,handle404
from routes import routes
app = Flask(__name__)
api = flask_restful.Api(app)

setroutes(api,routes)
handle404(app,api)

if __name__ == '__main__':
    app.run(debug=debug, host = host_ip, port = host_port)
