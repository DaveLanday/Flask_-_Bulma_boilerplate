#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#views.py
#Dave Landay
#LAST UPDATED: 01-09-2020

from flask import Blueprint, url_for, render_template

mod = Blueprint('site', __name__, template_folder='templates')

# Routes to the homepage:
@mod.route('/')
def index():
    return render_template('index.html')

# Routes to the gallery page:
@mod.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Routes to the shop page
@mod.route('/shop')
def shop():
    return render_template('shop.html')

# Routes to the about page:
@mod.route('/about')
def about():
    return render_template('about.html')

