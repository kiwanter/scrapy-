import scrapy
import re,os
from learnp2.items import Learnp2Item
class QsbkSpider(scrapy.Spider):
    name = 'QSBK'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = 'https://www.qiushibaike.com'
    n = 0

    def parse(self, response):
        self.n+=1
        print(self.n)
        cont = response.xpath("//div[@id='content']//div[@class='col1 old-style-col1']/div")
        for x in cont:
            c = x.xpath(".//div[@class='content']//text()").getall()
            c = "".join(c).strip()
            #r = re.sub(r'[\n]+', r'\n',c)
            item = Learnp2Item(content = c)
            yield item
        next_url = response.xpath("//div[@class='col1 old-style-col1']/ul/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)
