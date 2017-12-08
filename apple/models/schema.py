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
    record = graphene.Field(RecordType, id=graphene.Int())
    records = graphene.List(
        RecordType,
        city_name=graphene.String(),
        area=graphene.String()
    )
    # all_records = SQLAlchemyConnectionField(RecordType)

    def resolve_record(self, info, **args):
        id = args.get('id')
        return RecordType.get_query(info).get(id)

    def resolve_records(self, info, **args):
        query = RecordType.get_query(info)
        return query.filter_by(**args)

schema = graphene.Schema(query=Query, types=[RecordType])
