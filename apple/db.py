# -*- coding: utf-8 -*-

import pandas as pd

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .instance.config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
session = DBSession()


def init():
    # TODO: Need to drop table here?
    Base.metadata.create_all(bind=engine)


def persist(klass, data, if_exists='replace'):
    columns = [c.name for c in klass.__table__.columns][1:]
    df = pd.DataFrame(data, columns=columns)
    df.to_sql(name=klass.__table__.name, con=engine, if_exists=if_exists, index=False)
