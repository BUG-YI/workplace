import urllib.request
import urllib.parse

"""
parse.quote(str)将字符串unicode编码
"""
str1 = urllib.parse.quote('zhangs')

#get
url_get = f'https://www.baidu.com/s?wd={str1}'

headers =  {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',

}


# requestObject = urllib.request.Request(url_get,headers=headers)
#
# response = urllib.request.urlopen(requestObject)
# print(response.read().decode())


#post
url_post = 'https://cn.bing.com/tsuggestions'
data = {
    'text':'hello'
}
encode = urllib.parse.urlencode(data).encode('utf-8')
requestObject = urllib.request.Request(url_post,encode,headers)

response = urllib.request.urlopen(requestObject)
content = response.read().decode('utf-8')
print(content)