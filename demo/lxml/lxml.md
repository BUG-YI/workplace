安装`lxml`库

```cmd
pip install lxml
```

### etree

解析本地html

```python
from lxml import etree
parse = etree.parse('本地html文件')
#text()获取标签中的内容
parse.xpath('./xpath路径/text()')

```



解析网络/远程文件

```python
from lxml import etree
etree.HTML('网络文件')
```



### xpath语法
```
    1. 路径查询
        // ：查找所有子孙节点，不考虑层级关系
        / ：查找直接子节点
    
    2. 谓词查询
        //div[@id]
        //div[@id=""]
        
    3. 属性查询
        //@class
        
    4. 模糊查询
        //div[contains(@id, "he")]
        //div[starts-with(@id, "he")]
        
    5. 内容查询
        //div/h1/text()
        
    6. 逻辑运算
        //div[@id="head" and @class="s_down"]
        //title | //price
```