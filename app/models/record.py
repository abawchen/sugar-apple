# from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
# from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()

# class Record(Base):
#     __tablename__ = 'record'
#     id = Column(Integer, primary_key=True)
#     # name = Column(String)
#     sn = Column(String)

# from sqlalchemy import create_engine
# engine = create_engine('mysql://root:54883155@127.0.0.1:3306/sugar-apple', echo=False)

# from sqlalchemy.orm import sessionmaker
# session = sessionmaker()
# session.configure(bind=engine)
# Base.metadata.create_all(engine)