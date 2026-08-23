from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'html/index.html')

def index_test(request):
    peoples = [
        {'name':'zhangs', 'age':18},
        {'name':'lis', 'age':20},
        {'name':'wangw', 'age':19},
    ]
    return render(request, 'html/index.html', context={'peoples':peoples})

def hello(request):
    return HttpResponse("<h1>hello world!</h1>")

def hello_world(request):
    return HttpResponse("""
    <h1>hello world!</h1>
    <p>start study django</p>
    """)

def block_start(request):
    return render(request, 'html/block_start.html')

def test(request):
    return render(request, "html/Test/placeholder.html")

def container(request):
    return render(request, "html/login.html")