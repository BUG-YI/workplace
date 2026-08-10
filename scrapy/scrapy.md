from scrapy.settings.default_settings import LOG_LEVELfrom scrapy.settings.default_settings import LOG_FILE安装scrapy模块

```cmd
pip install scrapy
```



### 创建scrapy爬虫项目

```cmd
scrapy startproject 项目名
```



项目结构

```text
myproject/                          # 项目根目录
├── scrapy.cfg                      # 项目配置文件
├── myproject/                      # 项目主模块
│   ├── __init__.py
│   ├── items.py                    # 定义数据模型
│   ├── middlewares.py              # 自定义中间件
│   ├── pipelines.py                # 数据管道处理，用于后期处理下载数据，
│   │                             默认优先级300，数值越小优先级越高,范围(1-1000)                                    
│   ├── settings.py                 # 项目设置，配置文件
│   ├── spiders/                    # 爬虫文件夹
│   │   ├── __init__.py
│   │   └── example_spider.py       # 爬虫文件，实现爬虫核心文件
│   └── __pycache__/                # Python 缓存
└── other_files/                    # 其他文件
```



关闭爬虫君子协议，修改文件settings.py

```python
#将其注释掉或者改成False
ROBOTSTXT_OBEY = True
```

创建项目

```cmd
#进入myproject主模块
#注意脚本名不加后缀
scrapy genspider 脚本名 网址
```

> [!NOTE]
> 如果网址或接口以.html后缀结尾，最好去掉最后面的`/`

生成脚本文件位置：项目名/项目名/spiders/脚本文件

```python
import scrapy


class BaiduSpider(scrapy.Spider):
    name = "脚本名"
    allowed_domains = ["域名"]
    start_urls = ["网站地址"]

    def parse(self, response):
        pass
```



运行爬虫

```cmd
scrapy crawl 脚本名  #注意脚本名不加后缀
```



### 项目名/项目名/spiders/爬虫文件 response属性和方法

#### 属性

1. response.text 字符串

```python
import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        context = response.text
```

2. response.body 二进制数据

```python
import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        context = response.body
```

3. response.xpath() xpath搜索

```python
import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        context_list = response.xpath('xpath表达式')
        context = context_list[0]
        print(context.extract())  #xpath解析response文本内容
```



### scrapy shell

在不运行爬虫代码的情况下调试xpath

需要高亮或自动补全，安装ipython

```cmd
pip install ipython
```



### item.py文件

定义数据结构

```python
import scrapy
from dataclasses import dataclass


@dataclass
class ScrapyProjectItem:
    # define the fields for your item here like:
    # name: str | None = None
    
    #eg:
    name: str
    image: str
```



### yield

yield 多次返回数据，
return 一次性返回数据

```python
#函数hello()逐步返回
def hello():
    for i in range(10):
        yield f'hello,number:{i}!'
```



### pipelines.py 管道

想要使用需要开启设置`settings.py`的设置,取消注释
```python
ITEM_PIPELINES = {
   "项目名.pipelines.ScrapyProjectPipeline": 300,
}
```



pipelines.py
```python
from itemadapter import ItemAdapter

class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        
        #在这个文件执行数据保存的io操作
        
        return item
```
>[!note]
>上述方法每接收一个yield对象就会执行一次io操作
>```python
>from itemadapter import ItemAdapter
>
>
>class ScrapyProjectPipeline:
>    def __init__(self):
>        self.fp = None
>
>    def open_spider(self,spider):
>        self.fp = open(f'{spider.name}.json','w',encoding='utf-8')
>
>    def process_item(self, item, spider):
>
>        self.fp.write(str(item))
>
>        return item
>
>    def close_spider(self, spider):
>        self.fp.close()
>```



#### 多条管道

一个爬虫脚本，一个管道，多个爬虫脚本，为脚本创建类就行，类名自定义

```python
from itemadapter import ItemAdapter

#管道1
class ScrapyProjectPipeline:
    def __init__(self):
        self.fp = None

    def open_spider(self,spider):
        self.fp = open(f'{spider.name}.json','w',encoding='utf-8')

    

    def close_spider(self, spider):
        self.fp.close()

#管道2
class ScrapyMeiTuanPipeline:
    def process_item(self, item, spider):

        return item
```



setting.py中修改

```python
ITEM_PIPELINES = {
    #管道1
   "scrapy_project.pipelines.ScrapyProjectPipeline": 300,
    #添加新管道2
    "scrapy_project.pipelines.ScrapyMeiTuanPipeline": 301,
}
```



### 同域名爬取多页

#### Get请求
scrapy.Request()

url 网站接口地址

callback 调用的函数，不要加`()`

一定 要有退出条件

```python
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

        if self.page <3:
            self.page +=1
            others_url = f"https://www.readnovel.com/category/30036_f1_1_f1_f1_f1_0_{self.page}"
            
            yield scrapy.Request(url=others_url,callback=self.parse)
```



#### Post请求

scrapy中用start_requests()函数发送post请求


```python
import scrapy
from scrapy import FormRequest

from ..items import ScrapyProjectItem

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    # start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        pass
    def start_requests(self):
        url = ''
        data = {

        }

        yield FormRequest(url=url,formdata=data,callback=self.parse)

```



#### scrapy.Request meta属性

meta 向其他回调函数传递参数

```python
import scrapy
from ..items import ScrapyProjectItem


class ReadnovelSpider(scrapy.Spider):
    name = "readnovel"
    allowed_domains = ["www.readnovel.com"]
    start_urls = ["https://www.readnovel.com/category/30036_f1_1_f1_f1_f1_0_1"]

    page = 1

    def parse(self, response):

        title_list = response.xpath(
            '//div[@class="book-info"]/h3/a[not(preceding-sibling::a) and text()[normalize-space()]]/@title').getall()
        image_list = response.xpath('//div[@class="book-img"]/a/img/@src').getall()
        for i, j in zip(title_list, image_list):
            print(i, f":https:{j}")
            book = ScrapyProjectItem(image=j, name=i)

            yield book

        if self.page < 3:
            self.page += 1
            others_url = f"https://www.readnovel.com/category/30036_f1_1_f1_f1_f1_0_{self.page}"
            try:
                yield scrapy.Request(url=others_url, callback=self.parse)
            except:
                yield scrapy.Request(url=others_url, callback=self.parse_err, meta={'url': others_url})

    def parse_err(self, response):
        url_ = response.meta['url']
        yield ScrapyProjectItem(name=url_,err="请求失败")

```



### 其他文件使用`settings.py`中设置的参数

setting.py

```python
#可以随便找个位置写
db_name = 'mysql'
```

```python
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
s = settings["db_name"]
```



### scrapy日志

setting.py

```python
#控制台返回的数据将日志写入log.log文件
LOG_FILE = "log.log"

#一般不用
LOG_LEVEL = "warning"
```

> [!note]
>文件需要后缀`.log`
