# Django

## 安装

[Download Python | Python.org](https://www.python.org/downloads/)



```cmd
#在python环境中下载django软件包
pip install django

#在有django安装包的python环境中创建django项目
django-admin startproject 项目名
```



```cmd
#
python manage.py startapp home

#
python manage.py startapp account

#将创建的home，account目录添加到DjangoProject/DjangoProject/settings.py文件
#INSTALLED_APPS = [
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#    'account',
#    'home'
#]

#
python manage.py runserver
python manage.py runserver 0.0.0.0:5000

```



生成项目结构

```text
DjangoProject/                          # 项目根目录
├── manage.py                       # 命令行工具
├── DjangoProject/                      # 项目配置目录
│   ├── __init__.py                 # 空文件
│   ├── settings.py                 # 配置文件
│   ├── urls.py                     # URL 路由
│   ├── asgi.py                     # ASGI 入口
│   └── wsgi.py                     # WSGI 入口
├── templates/  
│ 
├── account/                          # 应用目录
│   ├── __init__.py                 # 空文件
│   ├── admin.py                    # 后台管理
│   ├── apps.py                     # 应用配置
│   ├── models.py                   # 数据模型
│   ├── views.py                    # 视图
│   ├── tests.py                    # 测试
│   └── migrations/                 # 迁移文件夹
│       └── __init__.py             # 空文件
│ 
├── home/                          # 应用目录
│   ├── __init__.py                 # 空文件
│   ├── admin.py                    # 后台管理
│   ├── apps.py                     # 应用配置
│   ├── models.py                   # 数据模型
│   ├── views.py                    # 视图
│   ├── tests.py                    # 测试
│   └── migrations/                 # 迁移文件夹
│       └── __init__.py             # 空文件
└── db.sqlite3                      # 数据库文件（运行后生成）
```



### 项目启动

在home目录下创建`templates`存放html，css，javascript文件资源

创建相应文件夹

```text
home/                      
│   ├── __init__.py        
│   ├── admin.py           
│   ├── apps.py            
│   ├── models.py          
│   ├── views.py           
│   ├── tests.py    
│   ├── templates/
│   │   ├── html
│   │   │   ├── index.html
│   │   ├── css
│   │   ├── js
│   │   └── __init__.py    
│   └── migrations/        
│       └── __init__.py    
```



#### 让网页文件显示

home/templates/html/index.html

```html
<!--html内容自己写-->
```

home/views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

"""
1. render() 方式返回整个文件
2. HttpResponse() 返回html标签格式的文本
"""
def index(request):
    return render(request, 'html/index.html')

def hello(request):
    return HttpResponse("<h1>hello world!</h1>")

def hello_world(request):
    return HttpResponse("""
    <h1>hello world!</h1>
    <p>start study django</p>
    """)
```

DjangoProject/DjangoProject/urls.py

```text
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", index, name='index'),
    path("hello/", hello, name='hello'),
    path('hello-world/', hello_world, name='hello-world')
]
```



#### 向网页传输数据

```python
def index(request):
    peoples = [
        {'name':'zhangs', 'age':18},
        {'name':'lis', 'age':20},
        {'name':'wangw', 'age':19},
    ]
    
    return render(request, 'html/index.html', context={'peoples':peoples})
```



html模板中用`{{  }}`接收数据

```html
<p>{{ peoples }}</p>
```



### django模板

#### for循环

类似python for循环

```html
{% for i in peoples %}
<p>{{ i.name }}</p>
<br>
{% endfor %}
```



#### forloop.counter计数器

```html
{% for i in peoples %}
<p>{{ forloop.counter }}</p>
<br>
{% endfor %}
```



#### if判断

```html
{% for i in peoples %}
    {% if i.age > 1 %}
    <p>{{ i.age }},age+1: {{ i.age|add:1 }}</p>
    {% endif %}
{% endfor %}
```



### block start

有相同的，可重复使用的

设置基础复用页面

home/templates/html/base.html

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
{% block start %}

{% endblock %}
</body>
</html>
```



使用

```html
{% extends "html/base.html" %}
{% block start %}
{#<h1>block start</h1>#}
<a href="/">index</a>
    <p>1esfs</p>
{% endblock %}
```



### models.py

用于创建数据表结构模型

以类的方式编写

models.py

```python
from django.db import models

# Create your models here.

"""
创建学生表
"""
class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    image = models.ImageField()
    email = models.EmailField()
    address = models.TextField()
```



创建迁移文件

```cmd
python manage.py makemigrations
```



执行迁移,创建数据表，生成表名为`home_student`

```cmd
python manage.py migrate
```



#### 查看数据表

默认数据库sqlite

1. django shell

```cmd
#进入django shell
python manage.py shell

#查看所有模型的对应的数据表
from django.db import connection
print(connection.introspection.table_names())
```



2. sqlite3

进入sqlite命令行

```cmd
sqlite3 db.sqlitee3
```

```sqlite
-- 查看所有表
.tables

-- 查看表结构，如table_name
.schema tablename

-- 查看表数据
select * from table_name;

-- 退出
.exit
```



#### 使用其他数据库，MySQL为例

Django/settings.py 更改设置

```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    #mysql,注意修改成自己的用户，密码，端口，数据库
    'default': {
        'ENGINE': 'django.db.backends.mysql',   #数据库引擎
        'NAME': 'Django',   #数据库
        "USER": 'root',     #用户名
        "PASSWORD": '1244231',  #密码
        "HOST": "localhost",    #主机地址
        "PORT": '3306',     #端口
        'OPTIONS': {
            'charset': 'utf8mb4'    #字符集
        }
    }
}
```



设置完成迁移数据结构，创建数据表

迁移只会迁移数据结构，旧数据需要自己导出/导入

>[!note]
> django版本对数据库版本有要求
> 
>django 5.x 要求MySQL8.4+

#### 向数据表中添加数据

```cmd
#进入django shell
python manage.py shell

#导入模块
from home.models import *

#编写数据
student = Student(name = 'zhangs', age = 20, email = '123@qq.com', address = 'Chongqing')

#保存数据
student.save()

#查看第一条数据的name
Student.objects.all()[0].name
```



home/models.py

```python
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    def __str__(self):
        return self.name
```

python manage.py shell 中使用 Student.objects.all()能直接打印`name`属性

#### django ORM查询

1. 类名.objects.all() 查询所有数据
2. 类名.objects.first() 查询第一条数据
3. 类名.objects.last() 查询最后一条数据
4. 类名.objects.filter(条件) 查询指定条件数据
5. 类名.objects.exclude(条件) 查询排除指定条件的其他所有数据
6. 类名.objects.count() 查询所有数据条数

```cmd
python manage.py shell

Student.objects.filter(age=18)

Student.objects.exclude(age=18)
```



### 加载静态文件

setting.py

```python
STATIC_URL = 'static/'

#必要配置
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

#生成环境收集目录，非必要
STATIC_ROOT = BASE_DIR / 'staticfiles'
```