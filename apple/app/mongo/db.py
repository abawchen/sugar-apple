# -*- coding: utf-8 -*-

import json
import pandas as pd

from pymongo import MongoClient

from ..instance.config import MONGO_DATABASE_URI

client = MongoClient(MONGO_DATABASE_URI)
db = client['sugar-apple']

def persist(model, data):
    collection = model.__dict__.get('_meta').get('collection')
    columns = [c for c in model.__dict__.get('_fields_ordered')][1:]
    df = pd.DataFrame(data, columns=columns)
    # https://stackoverflow.com/a/20167984/9041712
    records = json.loads(df.T.to_json()).values()
    try:
        db[collection].insert(records)
    except Exception as e:
        # XXX: No operations to execute raised.
        pass


# class Todo(client.Document):
#     title = db.StringField(max_length=60)
#     text = db.StringField()
#     done = db.BooleanField(default=False)
#     pub_date = db.DateTimeField(default=datetime.datetime.now)
