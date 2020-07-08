import scrapy
from RedirecTest.items import RedirectestItem
from selenium import webdriver


class IcbcUsSpider(scrapy.Spider):
    name = 'icbc-us'
    #allowed_domains = ['icbc-us.com']
    start_urls = ['http://www.icbc-us.com']

    def __init__(self):
        print('starting......')
        self.browser = webdriver.Chrome(executable_path='E:\chromedriver\chromedriver.exe')
        super().__init__()


    def close(self,spider):
        print('closing......')
        self.browser.quit()

    def parse(self, response):
        print('=' * 100)
        print(response.text)
        print('=' * 100)
