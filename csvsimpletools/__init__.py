# coding: utf-8

from flask import Flask
from flask.ext.script import Manager
from flask_wtf.csrf import CsrfProtect

app = Flask('csvsimpletools')
app.config.from_object('config')
manager = Manager(app)
CsrfProtect(app)

from csvsimpletools import views
