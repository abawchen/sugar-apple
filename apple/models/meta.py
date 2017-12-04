from sqlalchemy import create_engine, Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension

Base = declarative_base()
# DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension))

# engine = create_engine('mysql://root:54883155@127.0.0.1:3306/sugar-apple', echo=False)
# https://stackoverflow.com/a/44936870/9041712
engine = create_engine('mysql+mysqldb://root:54883155@127.0.0.1:3306/sugar-apple', echo=False)
# Base.metadata.create_all(bind=engine)
