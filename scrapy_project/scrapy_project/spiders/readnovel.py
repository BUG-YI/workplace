import scrapy
from ..items import ScrapyProjectItem


class ReadnovelSpider(scrapy.Spider):
    name = "readnovel"
    allowed_domains = ["www.readnovel.com"]
    start_urls = ["https://www.readnovel.com/category/30036_f1_1_f1_f1_f1_0_1"]

    page = 1
    def parse(self, response):

        title_list = response.xpath('//div[@class="book-info"]/h3/a[not(preceding-sibling::a) and text()[normalize-space()]]/@title').getall()
        image_list = response.xpath('//div[@class="book-img"]/a/img/@src').getall()
        for i,j in zip(title_list,image_list):
            print(i,f":https:{j}")
            book = ScrapyProjectItem(image=j, name= i)

            yield book

        if self.page<3:
            self.page +=1
            others_url = f"https://www.readnovel.com/category/30036_f1_1_f1_f1_f1_0_{self.page}"
            yield scrapy.Request(url=others_url,callback=self.parse)

