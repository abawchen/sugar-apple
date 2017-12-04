from .meta import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, Numeric, ForeignKey, func

class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)

    # 縣市代碼
    city_code = Column(String(2))

    # 城市名稱
    city_name = Column(String(64))
