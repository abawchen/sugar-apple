import scrapy
import re

from real_estate.items import RealEstateItem

class YungchingSpider(scrapy.Spider):
    name = 'yungching'
    allowed_domains = ['buy.yungching.com.tw']
    start_urls = [
        'https://buy.yungching.com.tw/region/台北市-_c/?pg=345'
    ]

    def parse(self, response):
        for record in response.css('li.m-list-item'):
            item = RealEstateItem()
            item['agent'] = self.name
            item['list_price'] = record.css('span.price-num::text').extract_first().replace(',', '')

            title = record.css('h3::text').extract_first()
            item['name'], item['address'] = title.split('　')
            item['city_name'], item['area'] = re.findall(r'\w{3}', item['address'])[:2]

            description = record.css('div.item-description::text').extract_first()
            item['sn'], item['description'] = description.split('  ', maxsplit=1)

            detail = record.css('ul.item-info-detail')
            details = [v.strip() for v in detail.css('li::text').extract()]
            if len(details) < 9:
                details += [''] * (9 - len(details))
            item['category'], item['age'], item['floor'], \
            item['land_ping'], item['main_ping'], item['building_ping'], \
            item['layout'], item['added_layout'], item['parking_lot'] = \
                details
            yield item

        active = response.css('li.is-active')
        page_no = int(re.findall('pg=(\d+)', response.url)[0])
        disabled = response.css('li.disabled')
        if disabled and disabled.css('a::text').extract_first() == '下一頁 >':
            return

        next_page_url = re.sub('pg=(\d+)', 'pg=' + str(page_no + 1), response.url)
        yield scrapy.Request(url=next_page_url)
