# -*- coding: utf-8 -*-
# https://stackoverflow.com/a/45613994/9041712

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..instance.config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)

Base = declarative_base()
# Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

from .city import City
from .record import Record