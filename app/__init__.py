#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#__init__.py
#Dave Landay
#LAST UPDATED: 01-11-2020

from flask import Flask
from app.site.view import mod

app = Flask(__name__, static_folder='site/static')
app.config.from_pyfile('config.py')

app.register_blueprint(mod)
