import urllib.request

url = 'https://www.baidu.com'
headers =  {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',

}

requestObject = urllib.request.Request(url,headers=headers)

proxy = {

}

#获取handle对象
handler = urllib.request.ProxyHandler(proxies=proxy)

#获取opener对象
opener = urllib.request.build_opener(handler)

#调用open方法
response = opener.open(requestObject)

print(response.read().decode())