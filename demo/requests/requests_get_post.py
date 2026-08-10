import requests

url = 'https://www.baidu.com'

headers =  {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

data = {

}

#requests中参数不用编码
res = requests.get(url,params=data,headers=headers)

context = res.text
print(context)