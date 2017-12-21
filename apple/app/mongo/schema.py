# -*- coding: utf-8 -*-
# https://medium.com/@fasterpancakes/graphql-server-up-and-running-with-50-lines-of-python-85e8ada9f637

import graphene
import mongoengine

from .models import Record
from ..instance.config import MONGO_DATABASE_URI

# http://docs.mongoengine.org/guide/connecting.html
mongoengine.connect('sugar-apple', host=MONGO_DATABASE_URI, alias='default')

def construct(object_type, mongo_obj):
    field_names = [f.attname for f in object_type._meta.fields]
    if 'id' in field_names:
        field_names.append('_id')
    kwargs = {attr: val for attr, val in mongo_obj.to_mongo().items()
              if attr in field_names}
    if '_id' in kwargs:
        kwargs['id'] = kwargs.pop('_id')
    return object_type(**kwargs)


class RecordField(graphene.ObjectType):

    id = graphene.String()
    trading_type = graphene.String()
    city_code = graphene.String()
    city_name = graphene.String()


class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()
    record = graphene.Field(
        RecordField, city_code=graphene.Argument(graphene.String))
    records = graphene.List(
        RecordField,
        limit=graphene.Int(),
        offset=graphene.Int(),
        city_code=graphene.String(),
        area=graphene.String()
    )

    # def resolve_record(self, info, **args):
    #     city_code = args.get('city_code')
    #     # print(city_code)
    #     return Record.objects.get(city_code=city_code)

    def resolve_records(self, info, **args):
        city_code = args.get('city_code')
        limit = args.pop('limit', 0)
        offset = args.pop('offset', 0)
        records = Record.objects.filter(city_code=city_code)
        return records

schema = graphene.Schema(query=Query)
