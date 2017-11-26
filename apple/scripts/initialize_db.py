from models.meta import Base
from sqlalchemy import create_engine

engine = create_engine('mysql://root:54883155@127.0.0.1:3306/sugar-apple', echo=False)
Base.metadata.create_all(bind=engine)