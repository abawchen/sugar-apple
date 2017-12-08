# -*- coding: utf-8 -*-

import pandas as pd

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .instance.config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


def init():
    # TODO: Need to drop table here?
    Base.metadata.create_all(bind=engine)


def persist(model, data, if_exists='replace'):
    columns = [c.name for c in model.__table__.columns][1:]
    df = pd.DataFrame(data, columns=columns)
    s = df.to_sql(name=model.__table__.name, con=engine, if_exists=if_exists, index=False)#index=True, index_label='id')


def add_primary_key(model):
    # https://stackoverflow.com/a/40770849/9041712
    # https://blog.inferentialist.com/2016/12/04/serialized-sql-pandas.html
    with engine.connect() as con:
        con.execute('ALTER TABLE `' + model.__table__.name + '` ADD `id` int(11) AUTO_INCREMENT PRIMARY KEY FIRST;')
