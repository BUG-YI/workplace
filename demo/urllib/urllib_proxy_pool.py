import urllib.request
import random

url = 'https://www.baidu.com'
headers =  {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',

}

requestObject = urllib.request.Request(url,headers=headers)

proxy_pool = [
    {'http':'192.168.1.1:8888'},
    {'http':'192.168.1.2:8888'}
]

#随机获取代理池中的代理ip
proxy = random.choice(proxy_pool)


#获取handle对象
handler = urllib.request.ProxyHandler(proxies=proxy)

#获取opener对象
opener = urllib.request.build_opener(handler)

#调用open方法
response = opener.open(requestObject)

print(response.read().decode())