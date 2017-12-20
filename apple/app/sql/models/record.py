from ..db import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, Numeric, Float, ForeignKey, func

class Record(Base):
    __tablename__ = 'record'

    id = Column(Integer, primary_key=True)

    ### Custom fields
    # 交易類別
    trading_type = Column(String(16))

    # 城市代碼
    city_code = Column(String(2))

    # 城市名稱
    city_name = Column(String(64))

    # 經度
    lng = Column(Numeric)

    # 緯度
    lat = Column(Numeric)

    ### Parsing fields
    # 鄉鎮市需
    area = Column(String(64))

    # 交易標的
    trading_target = Column(String(64))

    # 土地區段位置或建物區門牌
    address = Column(String(256))

    # 土地移轉總面積平方公尺
    land_total_sqare_meter = Column(Float(precision=2))

    # 都市土地使用分區
    urban_land_usage = Column(String(8))

    # 非都市土地使用分區
    non_urban_land_usage = Column(String(8))

    # 非都市土地使用編定
    non_urban_land_sn = Column(String(32))

    # 交易年月日
    trading_date = Column(String(16))

    # 交易筆棟數
    trading_detail = Column(String(64))

    # 移轉層次
    floor = Column(String(32))

    # 總樓層數
    total_floor = Column(String(32))

    # 建物型態
    building_type = Column(String(64))

    # 主要用途
    building_purpose = Column(String(32))

    # 主要建材
    building_material = Column(String(64))

    # 建築完成年月
    completion_date = Column(String(16))

    # 建物移轉總面積平方公尺
    building_total_sqare_meter = Column(Float(precision=2))

    # 建物現況格局-房
    number_of_bedroom = Column(Integer)

    # 建物現況格局-廳
    number_of_room = Column(Integer)

    # 建物現況格局-衛
    number_of_bathroom = Column(Integer)

    # 建物現況格局-隔間
    number_of_compartment = Column(String(8))

    # 有無管理組織
    management_committee = Column(String(1))

    # 總價元
    total_price = Column(Numeric)

    # 單價每平方公尺
    price_per_square_meter = Column(String(64))

    # 車位類別
    parking_space_type = Column(String(32))

    # 車位移轉總面積平方公尺
    parking_space_square_meter = Column(Float(precision=2))

    # 車位總價元
    parking_space_price = Column(Numeric)

    # 備註
    notes = Column(String(512))

    # 編號
    sn = Column(String(256))
