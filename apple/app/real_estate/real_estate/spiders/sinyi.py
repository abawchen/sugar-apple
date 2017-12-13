# -*- coding: utf-8 -*-

import scrapy
import re

from real_estate.items import RealEstateItem

class SinyiSpider(scrapy.Spider):
    name = 'sinyi'
    allowed_domains = ['buy.sinyi.com.tw']
    root_url = 'http://buy.sinyi.com.tw/list/'
    # http://buy.sinyi.com.tw/list/Taipei-city/index.html
    def start_requests(self):
        # XXX: Hardcode here.
        cities = [
            'Taipei-city', 'NewTaipei-city', 'Taoyuan-city',
            'Hsinchu-city', 'Hsinchu-county', 'Keelung-city',
            'Taichung-city', 'Changhua-county', 'Miaoli-county',
            'Nantou-county', 'Yunlin-county',
            'Kaoshiung-city', 'Tainan-city', 'Chiayi-city',
            'Chiayi-county', 'Pingtung-county',
            'Yilan-county', 'Hualien-city', 'Taitung-county',
            'Penghu-county', 'Kinmen-county'
            'Kinmen-county'
        ]
        for city in cities:
            url = self.root_url + city + '/1.html'
            yield scrapy.Request(url=url, dont_filter = True)

    def parse(self, response):
        for record in response.css('div.search_result_item'):
            item = RealEstateItem()
            item['agent'] = self.name

            item['list_price'] = record.css('span.num::text').extract_first().replace(',', '')
            item['name'] = record.css('span.item_title::text').extract_first()
            item['sn'] = record.css('span.item_title').xpath('@title').extract_first().split(' - ')[-1]
            item['url'] = record.css('div.search_result_item > a').xpath('@href').extract_first()

            detail_line1 = record.css('div.detail_line1')
            details = [v.strip() for v in detail_line1.css('span::text').extract()]
            # XXX: Take care bad data.
            details += [''] * max(0 ,(3 - len(details)))
            item['address'], item['category'], item['parking_lot'] = \
                details

            detail_line2 = record.css('div.detail_line2')
            if not item['category'] or len(detail_line2) < 2:
                # 土地買賣
                if not item['category']:
                    item['category'] = '土地'
            else:
                # details = [v.strip() for v in detail_line2[0].css('span::text').extract()]
                # print(details)
                details = detail_line2[0].css('span.num::text').extract()
                # XXX: Take care bad data.
                details += [''] * max(0 ,(4 - len(details)))
                item['building_ping'], item['main_ping'], item['age'], item['floor'] = \
                    details
                layout = detail_line2[1].css('span.num::text').extract()
                zipped = zip(layout, ['房', '廳', '衛', '室'])
                # https://stackoverflow.com/a/3205524/9041712
                item['layout'] = ''.join(sum(zipped, ()))

            item['city_name'], item['area'] = re.findall(r'\w{3}', item['address'])[:2]
            yield item

        # Notes: Take care paging.
        try:
            current_page = int(response.css('li.page.current::text').extract_first())
            last_page = int(response.css('li.page::text').extract()[-1])
            if current_page == last_page:
                return

            next_page_url = re.sub('(\d+).html', str(current_page + 1) + '.html', response.url)
            yield scrapy.Request(url=next_page_url)
        except Exception as e:
            pass
