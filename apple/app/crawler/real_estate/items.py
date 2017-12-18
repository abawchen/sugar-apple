# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealEstateItem(scrapy.Item):
    # 仲介
    agent = scrapy.Field()

    # 縣市
    city_name = scrapy.Field()

    # 區
    area = scrapy.Field()

    # 建案名稱
    name = scrapy.Field()

    # 地址
    address = scrapy.Field()

    # 仲介物件編號
    sn = scrapy.Field()

    # 描述
    description = scrapy.Field()

    # 開價
    list_price = scrapy.Field()

    # 公寓、電梯大樓
    category = scrapy.Field()

    # 屋齡
    age = scrapy.Field()

    # 樓層
    floor = scrapy.Field()

    # 土地（坪）
    land_ping = scrapy.Field()

    # 主+陽（坪）
    main_ping = scrapy.Field()

    # 建物（坪）
    building_ping = scrapy.Field()

    # 格局, ex: 1房(室)2廳1衛
    layout = scrapy.Field()

    # 加蓋格局
    added_layout = scrapy.Field()

    # 車位
    parking_lot = scrapy.Field()

    # 網址
    url = scrapy.Field()
