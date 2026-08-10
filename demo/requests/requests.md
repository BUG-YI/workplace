安装requests模块

```cmd
pip install requests
```



### 使用

```python
import requests

url = 'https://www.baidu.com'

# 获取网页
response = requests.get(url)

# 设置响应编码格式
response.encoding = "utf-8"

# 返回string形式网页响应源码
context = response.text

#返回url地址
url_address = response.url

#返回二进制数据
two_data = response.content

#返回状态码
response_status = response.status_code

#返回响应头
response_headers = response.headers
```



### requests get/post请求

requests中参数不用编码

#### get请求

```python
import requests

url = 'https://www.baidu.com'

headers =  {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

data = {
    
}

response = requests.get(url=url,headers=headers,params=data)

context = response.text
```



#### post请求

```python
import requests

url = 'https://www.baidu.com'

headers =  {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

data = {
    
}

response = requests.post(url=url,headers=headers,data=data)

context = response.text
```



### requests proxy

```python
import requests

url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

data = {

}

proxy = {
    #"协议":"代理地址:端口"
    "http":"proxy address:port"
}

requests.post(url,data=data,headers=headers,proxies=proxy)
```



### requests session

请求为session对象,用于保持会话连接，多个请求之间共享连接

```python
import requests

url = '网址地址'

session = requests.session()

session.get(url)

session.close()
```