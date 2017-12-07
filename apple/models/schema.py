# -*- coding: utf-8 -*-
# https://medium.com/@fasterpancakes/graphql-server-up-and-running-with-50-lines-of-python-85e8ada9f637

import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from . import City, Record
from ..db import db_session

class CityType(SQLAlchemyObjectType):

    class Meta:
        model = City
        interfaces = (graphene.relay.Node, )

class RecordType(SQLAlchemyObjectType):

    class Meta:
        model = Record
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()

    record = graphene.Field(RecordType, id = graphene.Int())
    all_records = SQLAlchemyConnectionField(RecordType)

    def resolve_record(self, info, **args):
        id = args.get('id')
        query = RecordType.get_query(info)
        return query.get(id)

schema = graphene.Schema(query=Query, types=[RecordType])
