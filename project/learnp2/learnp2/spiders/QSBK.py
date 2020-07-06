import scrapy
from scrapy.http.response.html import HtmlResponse

class QsbkSpider(scrapy.Spider):
    name = 'QSBK'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        cont = response.xpath("//div[@id='content']//div[@class='col1 old-style-col1']/div//div[@class='content']/span")
        print("=" * 40)
        for x in cont:
            print(x.xpath("string(.)").get())
            #print(x.xpath(".//div[@class='content']/span/text()").get())
            # c=x.xpath("//div[@class='content']/span/text()")
            # print(c)
        print("=" * 40)
