# -*- coding: utf-8 -*-

import scrapy
import re

from real_estate.items import RealEstateItem

class YungchingSpider(scrapy.Spider):
    name = 'yungching'
    allowed_domains = ['buy.yungching.com.tw']
    root_url = 'https://buy.yungching.com.tw/region/'
    # start_urls = [
    #     'https://buy.yungching.com.tw/region/台北市-_c/?pg=1'
    # ]

    def start_requests(self):
        # XXX: Hardcode here.
        cities = [
            '南投縣', '嘉義市', '嘉義縣', '基隆市', '宜蘭縣',
            '屏東縣', '彰化縣', '新北市', '新竹市', '新竹縣',
            '桃園市', '澎湖縣', '台中市', '台北市', '台南市',
            '台東縣', '花蓮縣', '苗栗縣', '連江縣', '金門縣',
            '雲林縣', '高雄市'
        ]
        # XXX: Yungching does not have '連江縣'
        cities.remove('連江縣')
        for city_name in cities:
            url = self.root_url + city_name + '_c/?pg=1'
            yield scrapy.Request(url=url)

    def parse(self, response):
        for record in response.css('li.m-list-item'):
            item = RealEstateItem()
            item['agent'] = self.name
            item['list_price'] = record.css('span.price-num::text').extract_first().replace(',', '')

            title = record.css('h3::text').extract_first()
            item['name'], item['address'] = title.split('　', maxsplit=1)
            item['city_name'], item['area'] = re.findall(r'\w{3}', item['address'])[:2]

            description = record.css('div.item-description::text').extract_first()
            item['sn'], item['description'] = description.split('  ', maxsplit=1)

            detail = record.css('ul.item-info-detail')
            details = [v.strip() for v in detail.css('li::text').extract()]
            # XXX: Take care bad data.
            details += [''] * max(0 ,(9 - len(details)))
            item['category'], item['age'], item['floor'], \
            item['land_ping'], item['main_ping'], item['building_ping'], \
            item['layout'], item['added_layout'], item['parking_lot'] = \
                details
            yield item

        # Notes: Take care paging.
        active = response.css('li.is-active')
        try:
            page_no = int(re.findall('pg=(\d+)', response.url)[0])
            disabled = response.css('li.disabled')
            if disabled and disabled.css('a::text').extract_first() == '下一頁 >':
                return

            next_page_url = re.sub('pg=(\d+)', 'pg=' + str(page_no + 1), response.url)
            yield scrapy.Request(url=next_page_url)
        except Exception as e:
            pass
