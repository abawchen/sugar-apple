from flask import abort
from mongoengine import *
from mongoengine.fields import StringField, FloatField, DecimalField


class BaseQuerySet(QuerySet):
    """
    A base queryset with handy extras
    """

    def get_or_404(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except (MultipleObjectsReturned, DoesNotExist, ValidationError):
            abort(404)

    def first_or_404(self):

        obj = self.first()
        if obj is None:
            abort(404)

        return obj


class Record(Document):

    meta = {'collection': 'record'}

    ### Custom fields
    # 交易類別
    trading_type = StringField(max_length=16)

    # 城市代碼
    city_code = StringField(max_length=2)

    # 城市名稱
    city_name = StringField(max_length=64)

    # 經度
    lng = FloatField()

    # 緯度
    lat = FloatField()

    ### Parsing fields
    # 鄉鎮市需
    area = StringField(max_length=64)

    # 交易標的
    trading_target = StringField(max_length=64)

    # 土地區段位置或建物區門牌
    address = StringField(max_length=256)

    # 土地移轉總面積平方公尺
    land_total_sqare_meter = DecimalField(precision=2)

    # 都市土地使用分區
    urban_land_usage = StringField(max_length=8)

    # 非都市土地使用分區
    non_urban_land_usage = StringField(max_length=8)

    # 非都市土地使用編定
    non_urban_land_sn = StringField(max_length=32)

    # 交易年月日
    trading_date = StringField(max_length=16)

    # 交易筆棟數
    trading_detail = StringField(max_length=64)

    # 移轉層次
    floor = StringField(max_length=32)

    # 總樓層數
    total_floor = StringField(max_length=32)

    # 建物型態
    building_type = StringField(max_length=64)

    # 主要用途
    building_purpose = StringField(max_length=32)

    # 主要建材
    building_material = StringField(max_length=64)

    # 建築完成年月
    completion_date = StringField(max_length=16)

    # 建物移轉總面積平方公尺
    building_total_sqare_meter = DecimalField(precision=2)

    # 建物現況格局-房
    number_of_bedroom = IntField()

    # 建物現況格局-廳
    number_of_room = IntField()

    # 建物現況格局-衛
    number_of_bathroom = IntField()

    # 建物現況格局-隔間
    number_of_compartment = StringField(max_length=8)

    # 有無管理組織
    management_committee = StringField(max_length=1)

    # 總價元
    total_price = FloatField()

    # 單價每平方公尺
    price_per_square_meter = StringField(max_length=64)

    # 車位類別
    parking_space_type = StringField(max_length=32)

    # 車位移轉總面積平方公尺
    parking_space_square_meter = DecimalField(precision=2)

    # 車位總價元
    parking_space_price = FloatField()

    # 備註
    notes = StringField(max_length=512)

    # 編號
    sn = StringField(max_length=256)

    # meta = {
    #     'queryset_class': BaseQuerySet,
    #     'indexes': [
    #         {'fields': ('merchant_id', 'order_id'), 'unique': True}
    #     ]
    # }
