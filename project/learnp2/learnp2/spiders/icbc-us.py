import scrapy


class Learnp21Spider(scrapy.Spider):
    name = 'learnp2-1'
    allowed_domains = ['www.icbc-us.com']
    start_urls = ['http://www.icbc-us.com/']

    def parse(self, response):
        pass
