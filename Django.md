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
#创建home应用
python manage.py startapp home

#将创建的home，account目录添加到DjangoProject/DjangoProject/settings.py文件
#INSTALLED_APPS = [
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#    'home'
#]

#启动服务
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



##### JsonResponse 返回json数据

views.py

```python
from django.http import JsonResponse

def return_date(requset):
    return JsonResponse({json数据格式内容})
```



#### redirect 网页重定向

```python
from django.shortcuts import render, redirect

def rediect_html(request):
    return redirect('url中的name值（重定向的html）')  #不能返回数据
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
<!-- start 可自定义 -->
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



#### 继承

不继承内容会直接覆盖

```html
{% block start %}
{# 保留父级内容，追加新内容 #}
	{% block.super %}
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



### 查看数据表/数据库

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



#### 数据表CRUD

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



##### Create创建

models.py

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
```



views.py

```python
#导入model
from home.models import Student

#class.objects.create 创建完自动保存
def text(request):
    user = request.user
    Student.objects.create(
        user=user,
        name= 'zhangs',
        age= 18
    )
```



##### Update更新

views.py

```python
#导入model
from home.models import Student

#class.objects.update_or_create 更新或创建
#update 对象
#created 返回是否是创建
def text(request):
    user = request.user
    update,created = Student.objects.updata_or_create(
        user=user,
        name= 'zhangs',
        age= 18
    )
```



##### Delete删





##### Read查







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



### 向后端发送请求

```html
<form action="{% url 'path()函数的name值' %}" method="post">
<!--    必要-->
    {% csrf_token %}
    
    #后端通过name值获取数据
    <input type="text" name="example_name">
</form>
```

views.py 中的该路径函数

```python
def example_def(request):
    #需要大写
    if request.method == 'POST':
        example_name = request.POST.get("example_name")
    
    return render(request, 'html文件路径')
```



### message内置消息模块

setting.py

```python
INSTALLED_APPS = [
    ...
    'django.contrib.messages',  # 确保已添加
]

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',  # 消息依赖 Session
    'django.contrib.messages.middleware.MessageMiddleware',  # 消息中间件
]

TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.contrib.messages.context_processors.messages',  # 模板中使用 messages 变量
            ],
        },
    },
]
```



### Auth用户控制

#### 一对一

含义：A 表中的一条记录，对应 B 表中的一条记录。

适用场景：扩展用户信息、身份证与公民、商品与商品详情。

models.py

```python
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    #一对一
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null=True, blank=True)

    first_name = models.CharField()
    last_name = models.CharField()
```

完成后， python manage.py makemigrations ， python manage.py migrate 

views.py

```python
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User

from .models import Account

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        email = data.get('user_email')
        password = data.get('password')
        password_again = data.get('password_again')
        check_input = data.get('check_input')
        content = {
            'first_name': first_name,
            'email': email,
            'password': password,
            'password_again': password_again,
        }
        if not email or not password or not password_again or not first_name or not last_name:
            messages.error(request, 'Please fill in all the information')
            return render(request,'html/register.html',content)

        #用于验证用户是否存在
        if User.objects.filter(username=email).exists():
            messages.error(request,'Email always existence!')
            return render(request, 'html/register.html', content)
        
        if password != password_again:
            messages.error(request, "Twice password isn's same")
            return render(request, 'html/register.html', content)

        if not check_input:
            messages.error(request, 'Please check the user agreement ')
            return render(request,'html/register.html',content)

        user = User.objects.create_user(
            username = email,
            password=password
        )

        account = Account(
            user=user,
            first_name=first_name,
        )

        account.save()
        print('created successfully!')
        messages.success(request, 'Register successfully')
        return redirect('login')

    return render(request, 'html/register.html')
```

register.html

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'register.css' %}">
    <title>{% block title %}Document{% endblock %}</title>
</head>
<body class="p-3 m-0 border-0 bd-example m-0 border-0">
<div class="container container-min p-5 mx-auto border shadow" style="max-width: 40%;">
    <h1 class="text-center pb-3">Register</h1>
    <hr>
    {% if messages %}
        {% for m in messages %}
            {% if m.tags == 'error' %}
                <p class="text-danger text-shadow">{{ m }}</p>
            {% else %}
                <p class="text-success text-shadow">{{ m }}</p>
            {% endif %}
        {% endfor %}
    {% endif %}
    <form action="{% url 'register' %}" method="post">
        {% csrf_token %}
        <div class="row">
            <div class="col-5 mb-3">
                <div class="form-floating">
                    <input type="text" id="f_username" class="form-control focus-ring change-focus-ring" style="" placeholder="First Name" name="first_name" value="{{ first_name }}">
                    <label for="f_username" class="form-label">First Name</label>
                </div>
            </div>
        </div>
        <div class="form-floating mb-3">
            <input type="text" id="user_email" class="form-control focus-ring change-focus-ring" placeholder="Email Address" name="user_email" value="{{ email }}">
            <label for="user_email" class="form-label">Email Address</label>
        </div>
        <div class="form-floating mb-4">
            <input type="text" id="password" class="form-control focus-ring change-focus-ring" placeholder="Password" name="password" value="{{ password }}">
            <label for="password" class="form-label">Password</label>
        </div>
        <div class="form-floating mb-4">
            <input type="text" id="password2" class="form-control focus-ring change-focus-ring" placeholder="Password" name="password_again" value="{{ password_again }}">
            <label for="password2" class="form-label">Password Again</label>
        </div>
        <div class="row">
            <div class="col-8">
                <div class="form-check mb-3" style="font-size: 12px">
                    <input type="checkbox" id="agree" class="form-check-input focus-ring change-focus-ring" value="yes" name="check_input">
                    <label for="agree"></label>
                    <a href="#" class="shadow" data-bs-toggle="modal" data-bs-target="#modal">同意用户协议</a>
                    <div class="modal fade" id="modal">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <div class="modal-title fs-4">用户协议</div>
                                    <button class="btn-close" data-bs-dismiss></button>
                                </div>
                               <div class="modal-body" style="min-height: 300px; max-height: 300px;position: relative">
                                   <div style="min-height: 220px; max-height: 220px;overflow: auto">
                                       协议内容
                                   </div>
                               </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col" style="font-size: 13px">
                <a href="{% url 'login' %}" >Always has account</a>
            </div>
        </div>

        <div class="text-center">
            <button class="btn btn-success shadow">sign up</button>
        </div>

    </form>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
</body>
</html>
```



#### 一对多

含义：A 表中的一条记录，对应 B 表中的多条记录。

适用场景：一个作者有多篇文章、一个分类下有多个商品、一个部门有多个员工。


#### 多对多

含义：A 表中的一条记录，对应 B 表中的多条记录；反之亦然。

适用场景：学生与课程、文章与标签、用户与角色。

#### 用户认证

authenticate 验证数据库中是否有输入的账号
login 登入账号

views.py

```python
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('user_email')
        password = data.get('password')
        input_check = data.get('check_input')

        content =  {
            'email': email,
            'password': password
        }

        if not email or not password:
            messages.error(request,'Please fill in all the information')
            return render(request, 'html/login.html', content)

        if not input_check:
            messages.error(request, 'Please check the user agreement')
            return render(request, 'html/login.html', content)

        if not User.objects.filter(username=email).exists():
            messages.error(request, "Email or password is invalid")
            return redirect('login')
        user = authenticate(username=email, password=password)
        if user is None:
            return redirect('login')
        else:
            login(request, user=user)
            return redirect( 'index',)


    return render(request, 'html/login.html')
```

login.html

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'register.css' %}">
    <title>{% block title %}Document{% endblock %}</title>
</head>
<body class="p-3 m-0 border-0 bd-example m-0 border-0">
<div class="container container-min p-5 mx-auto border shadow" style="max-width: 40%;">
    <h1 class="text-center pb-3">Login</h1>
    <hr>
    {% if messages %}
        {% for m in messages %}
            {% if m.tags == 'error' %}
                <p class="text-danger">{{ m }}</p>
            {% else %}
                <p class="text-success">{{ m }}</p>
            {% endif %}
        {% endfor %}
    {% endif %}
    <form action="{% url 'login' %}" method="post">
        {% csrf_token %}
        <div class="form-floating mb-3">
            <input type="text" id="user_email" class="form-control focus-ring change-focus-ring" placeholder="Email Address" name="user_email" value="{{ email }}">
            <label for="user_email" class="form-label">Email Address</label>
        </div>
        <div class="form-floating mb-4">
            <input type="text" id="password" class="form-control focus-ring change-focus-ring" placeholder="Password" name="password" value="{{ password }}">
            <label for="password" class="form-label">Password</label>
        </div>
        <div class="row">
            <div class="col-9">
                <div class="form-check mb-3" style="font-size: 12px">
                    <input type="checkbox" id="agree" class="form-check-input focus-ring change-focus-ring" value="yes" name="check_input">
                    <label for="agree"></label>
                    <a href="#" class="shadow" data-bs-toggle="modal" data-bs-target="#modal">同意用户协议</a>
                    <div class="modal fade" id="modal">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <div class="modal-title fs-4">用户协议</div>
                                    <button class="btn-close" data-bs-dismiss></button>
                                </div>
                               <div class="modal-body" style="min-height: 300px; max-height: 300px;position: relative">
                                   <div style="min-height: 220px; max-height: 220px;overflow: auto">
                                       协议内容
                                       <p>1</p>
                                   </div>

                                   <div style="position: absolute; bottom: 10px; right: 10px">
                                       <button class="btn btn-danger">Refuse</button>
                                       <button class="btn btn-primary">Agree</button>
                                   </div>
                               </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col" style="font-size: 13px">
                <a href="{% url 'register' %}" >Go to sign up</a>
            </div>
        </div>

        <div class="text-center">
            <button class="btn btn-success shadow">login in</button>
        </div>

    </form>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
</body>
</html>
```


#### logout登出用户

views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_out(request):
    logout(request)
    return redirect('login')
```

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    {%  block style %}
    {% endblock %}
    <title>{% block title %}Document{% endblock %}</title>
    <style>
        .nav-color{
            background-color: rgb(200, 200, 200);
        }
    </style>
</head>
<body class="p-0 m-0 border-0 bd-example m-0 border-0">
<nav class="navbar navbar-expand-lg nav-color shadow-lg">
    <div class="container-fluid">
        <a href="#" class="navbar-brand">cqy</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav-title" aria-controls="nav-title" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div id="nav-title" class="collapse navbar-collapse" >
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a href="#" class="nav-link">case</a>
                </li>
            </ul>
            <div class="be">
                {% if request.user.is_authenticated %}
                    <a href="{% url 'logout' %}" class="btn btn-danger">logout</a>
                {% else %}
                    <a href="{% url 'login' %}" class="btn btn-success">login</a>
                {% endif %}
            </div>
        </div>
    </div>
</nav>
{% block start %}

{% endblock %}
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
</body>
</html>
```



#### login_required 检测用户是否登录

如果用户未登录重定向到某页面


views.py

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url='login')
def index(request):
    return render(request, 'html/index.html')
```



### 创建超级管理员

```cmd
python manage.py createsuperuser
```

网页路径：`ip address:8000/admin`


admin.py

注册数据表

```python
from django.contrib import admin

from .models import *

admin.site.register(Account)
```



### 聚合

Django ORM 中用于对查询集进行聚合计算的方法，比如计算总数、平均值、最大值、最小值等。

aggregate() 是 Django 查询集（QuerySet）的一个方法，用于返回一个包含聚合值的字典。它不会返回模型对象，而是返回计算结果。

| 函数  |	作用|示例|
|-----|    ----| ----|
Count|	计数	|统计用户数量
Sum	|求和	|计算订单总金额
Avg	|平均值	|计算平均年龄
Max	|最大值	|找出最高价格
Min	|最小值	|找出最低价格
StdDev	|标准差	|数据离散程度
Variance	|方差	|数据波动程度




```python
from django.db.models import Count, Sum, Avg, Max, Min

user_count = User.objects.all().aggregate(Count('id'))
```



#### annotate





### 上传文件

- **开发环境**：让 Django 直接提供用户上传的文件（图片、视频等）
- **生产环境**：通常由 Nginx、Apache 等 Web 服务器提供，Django 不处理

setting.py

```python
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 媒体文件配置
MEDIA_URL = '/media/'  # 访问URL
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

urls.py

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = []  #url路径

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



#### 图片重命名

生成唯一id

class 

```python
import os
import uuid
from django.utils.deconstruct import deconstructible

@deconstructible
class PictureRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        new_filename = f'{uuid.uuid4().hex}.{ext}'

        return os.path.join(self.path, new_filename)
```

models.py

```python
#导入上面文件

user_picture = models.ImageField(upload_to=PictureRename('user_picture/'), blank=True, null=True, default='default/user_default.png')
```



### 装饰器

#### @login_required

只有登录过后的才能访问



#### @csrf_exempt

跳过csrf验证



#### @cache_page(60)

缓存



#### @deconstructible

支持数据迁移，用于makemigrations，migrate



#### @admin.register

注册admin







## 问题集

### 手动删除数据表

删除数据表之后，出现`python manage.py migrate`报错

```
# 1. 查看迁移状态
python manage.py showmigrations

# 2. 伪造回滚到零（不执行 SQL，只更新记录）
python manage.py migrate flowers zero --fake

# 3. 删除迁移文件（保留 __init__.py）
rm flowers/migrations/0*.py  # Linux/macOS
del flowers\migrations\0*.py # Windows

# 4. 重新生成迁移
python manage.py makemigrations flowers

# 5. 执行迁移
python manage.py migrate flowers
```





# django-vue

常用3个包

```cmd
#Django REST Framework
pip install djangorestframework
#跨域支持
pip install django-cors-headers
#jwt认证
pip install djangorestframework-simplejwt
```



setting.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 第三方应用
    'rest_framework',  # DRF
    'rest_framework_simplejwt',  # JWT
    'corsheaders',  # CORS
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  #必须最前面
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS 配置
CORS_ALLOW_ALL_ORIGINS = True  # 开发环境（允许所有域名）
# CORS_ALLOWED_ORIGINS = [      # 生产环境（指定域名）
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
# ]

# REST Framework 配置
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# JWT 配置（可选）
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}
```



urls.py

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT Token 获取和刷新
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API 路由
    path('api/', include('flowers.urls')),
]
```



获取token密钥

```bash
POST /api/token/
{
    "username": "admin",
    "password": "123456"
}
```



刷新token

```
POST /api/token/refresh/
{
    "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```





## django

setting.py

在项目根目录下创建static用于存放静态文件和media 存放目录，图片资源

```python
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&zgr^2vf4y^hgz_qikgdmb!02*zws!&bijsjt4j8l35kat%r1i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 第三方应用
    'rest_framework',  # DRF
    'rest_framework_simplejwt',  # JWT
    'corsheaders',  # CORS

    'account',
    'flowers',
    'home',

    'app_test',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}

ROOT_URLCONF = 'DjangoApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 媒体文件配置
MEDIA_URL = '/media/'  # 访问URL
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

```



urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#页面返回路径
#''中写路径， 
#def_or_class 写vies.py 中的def 或 class， class 需要解析（class.as_view()）
urlpatterns = [
    path('', def_or_class, name= '')
]


#django返回可显示的图片等，
#生产环境一般由apache，nginx上线图片解析功能
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



### startapp

account



#### serializers.py

序列化

```python
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        
        #可选
        read_only_fields = []

    #我一般在前端验证数据，这里就没写数据验证
    
    def create(self, validated_data):
        
        if User.objects.fitlter(email= email).exists():
            return serializers.ValidstionError({
                'msg': '用户存在'
            })
            
        user = User.objects.create_user(
			# 根据自己需求写
        	username = validated_data['email']
            email = validated_data['email']
            password = validate_data['password']
        )
        
        return user
```



#### model.py

```python
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from utils.models.Rename import PictureRname

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.IntegerField(default=2)
    tel = models.IntegerField(blank=True, default=0)
    user_pic = models.ImageField(upload_to=PictureRname('user_picture/'), default='default/user_default.png')
    family_address = models.TextField(default='正在占据地球村...')
    hobby = models.TextField(default='寻找新明...')

    class Meta:
        db_table = 'account_profiles'
        ordering = ['-id']
        verbose_name = '用户'

```

数据迁移

```cmd
python manage.py makemigrations
python manage.py migrate
```



#### admin.py

注册模型

```python
from django.contrib import admin

from account.models import Profiles

admin.site.register(Profiles)
```





#### 创建超级用户

页面访问：http://127.0.0.1:8000/admin

```cmd
python manage.py createsuperuser
```







#### views.py

```python
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from utils.serializers import RegisterSerializer

class RegisteView(generics.CreateAPIView):
    queryser = User.objects.all()
    
    #允许任何人访问
    permissions_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'msg': 'user is success created'
            }, status = status.HTTP_200_OK)
            
        return Response({
            'msg': f'create is failed',
            'err': serializers.errors
        }, status = status.HTTP_400_BAD_REQUEST)
```



#### accout/urls.py

```python
from django.urls import path

from .models import *

urlpatterns = [
    path('register', RegisterView.as_view())
]
```



