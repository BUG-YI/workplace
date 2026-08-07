import urllib.request

url = 'https://www.baidu.com'

response = urllib.request.urlopen(url)

"""
read为二进制，decode解码 utf-8
"""
# print(response.read().decode("utf-8"))


"""
read()读取所有,read(number),读取number位
"""
# print('==========================+',response.read(13).decode("utf-8"),'===============')  #读取13位

"""
readline()读取整行
readlines()读取多行
"""
# print(response.readline())

"""
geturl()返回url address
getheaders()返回状态信息
"""
# print(response.geturl())
# print(response.getheaders())