import scrapy

from real_estate.items import RealEstateItem

class YungchingSpider(scrapy.Spider):
    name = 'yungching'
    allowed_domains = ['buy.yungching.com.tw']
    start_urls = [
        'https://buy.yungching.com.tw/region/台北市-_c/'
    ]

    def parse(self, response):
        for record in response.css('li.m-list-item'):
            item = RealEstateItem()
            title = record.css('h3::text').extract_first()
            item['name'], item['address'] = title.split('　')
            yield item

        # filename = response.url.split('/')[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)