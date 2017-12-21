# -*- coding: utf-8 -*-

from flask import Flask
from flask_graphql import GraphQLView

from .mongo.schema import schema as mongo_schema
from .mysql.db import db_session
from .mysql.models.schema import schema as mysql_schema


# https://spacewander.github.io/explore-flask-zh/5-configuration.html
app = Flask(__name__, instance_relative_config=False)
app.config.from_object('app.config')
app.config.from_pyfile('instance/config.py')
# app.config.from_envvar('APP_CONFIG_FILE')


@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/graphql-mongo', methods=['POST'])
# def query():
#     variables = request.json.get('variables') # Todo: add handling variables
#     logger.debug('Query: %s', request.json)
#     result = schema.execute(query)
#     result_hash = format_result(result)
#     return result_hash

app.add_url_rule(
    '/graphql-mongo', view_func=GraphQLView.as_view('graphql-mongo', schema=mongo_schema, graphiql=True))

app.add_url_rule(
    '/graphql-mysql', view_func=GraphQLView.as_view('graphql-mysql', schema=mysql_schema, graphiql=True, context={'session': db_session}))
"""
{
  records(limit: 5) {
    id,
    cityName
  }
}
"""

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# Run command:
# export FLASK_APP=app.py
# flask run -h 0.0.0.0 -p 5001
