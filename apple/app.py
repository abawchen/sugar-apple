# -*- coding: utf-8 -*-

from flask import Flask
from flask_graphql import GraphQLView
from .db import db_session
from .models.schema import schema


# https://spacewander.github.io/explore-flask-zh/5-configuration.html
app = Flask(__name__, instance_relative_config=False)
app.config.from_object('apple.config')
app.config.from_pyfile('instance/config.py')
# app.config.from_envvar('APP_CONFIG_FILE')


app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context={'session': db_session}))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



# Run command:
# export FLASK_APP=app.py
# flask run -h 0.0.0.0 -p 5001