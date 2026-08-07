import urllib.request
import urllib.parse

"""
parse.quote(str)将字符串unicode编码
"""
str1 = urllib.parse.quote('zhangs')

url = f'https://www.baidu.com/s?wd={str1}'

headers =  {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, ',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}
requestObject = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(requestObject)
print(response.read().decode())