# -*- coding: utf-8 -*-

from flask import Flask


# https://spacewander.github.io/explore-flask-zh/5-configuration.html
app = Flask(__name__, instance_relative_config=False)
app.config.from_object('apple.config')
app.config.from_pyfile('instance/config.py')
# app.config.from_envvar('APP_CONFIG_FILE')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# Run command:
# export FLASK_APP=app.py
# flask run -h 0.0.0.0 -p 5001