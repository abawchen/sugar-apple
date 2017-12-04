from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:54883155@127.0.0.1:3306/sugar-apple', echo=False)

Base = declarative_base()
# Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

from .city import City
from .record import Record