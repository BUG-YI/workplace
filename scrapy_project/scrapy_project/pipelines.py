# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyProjectPipeline:
    def __init__(self):
        self.fp = None

    def open_spider(self,spider):
        self.fp = open(f'{spider.name}.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == 'readnovel':
            context = str({
                item.name: item.image
            })
            self.fp.write(context)
            self.fp.write("\n")

        return item

    def close_spider(self, spider):
        self.fp.close()

from scrapy.utils.project import get_project_settings
class PP:
    def __init__(self):
        self.db = get_project_settings()['DB']

    def process_item(self, item, spider):

        if spider.name == 'baidu':

            print(self.db,'++++++++++++++++++++++++++++++++++=============')
        return item
