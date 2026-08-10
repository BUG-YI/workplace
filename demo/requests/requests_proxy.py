import requests

url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

data = {

}

proxy = {
    "http":"192.168.1.1:8888"
}

requests.post(url,data=data,headers=headers,proxies=proxy)
