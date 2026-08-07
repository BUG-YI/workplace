import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0'
}
requestObject = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(requestObject)

print(response.read().decode("utf-8"))