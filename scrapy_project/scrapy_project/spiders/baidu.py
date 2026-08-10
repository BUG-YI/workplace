import scrapy
from scrapy import FormRequest

from ..items import ScrapyProjectItem

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    # start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        yield ScrapyProjectItem(name='sd',image='ppp')

    def start_requests(self):
        url = ''
        data = {

        }

        yield FormRequest(url=url,formdata=data,callback=self.parse)
