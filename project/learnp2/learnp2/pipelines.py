# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
#json写法
# class Learnp2Pipeline:
#     def __init__(self):
#         pass
#
#     def open_spider(self,spider):
#         print('start crawl')
#         self.fp = open("text.json", 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
#
#     def close_spider(self,spider):
#         self.fp.close()
#         print('close crawl')


from scrapy.exporters import JsonItemExporter
#少量数据
# class Learnp2Pipeline:
#     def __init__(self):
#         pass
#
#     def open_spider(self,spoder):
#         print('start crawl')
#         self.fp = open("text.json", 'wb')#二进制打开
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def process_item(self,item,spider):
#         self.exporter.export_item(item)
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('close crawl')

from scrapy.exporters import JsonLinesItemExporter
#大量数据
class Learnp2Pipeline:
    def __init__(self):
        pass

    def open_spider(self,spoder):
        print('start crawl')
        self.fp = open("text.json", 'wb')#二进制打开
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print('close crawl')