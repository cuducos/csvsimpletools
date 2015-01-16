# coding: utf-8

from flask import Flask
from flask.ext.babel import Babel
from flask.ext.script import Manager
from flask_wtf.csrf import CsrfProtect

app = Flask('csvsimpletools')
app.config.from_object('config')
manager = Manager(app)
CsrfProtect(app)
babel = Babel(app)

if not app.config['DEBUG']:
    import logging
    from logging.handlers import RotatingFileHandler
    filepath = app.config['BASEDIR'].child('errors.log')
    handler = RotatingFileHandler(filepath, 'a', 1 * 1024 * 1024, 10)
    row = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(row)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.info('{} started successfully.'.format(app.config['TITLE']))

from csvsimpletools import views
