from .meta import Base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func

class Foo(Base):
    __tablename__ = 'foo'
    id = Column(Integer, primary_key=True)
    sn = Column(String(255))
