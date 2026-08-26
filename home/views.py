from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Account

@login_required(login_url='login')
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
    return render(request, "html/login_1.html")


def register_page(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('user_email')
        password = data.get('password')
        password_again = data.get('password_again')
        check_input = data.get('check_input')
        content = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'password_again': password_again,
        }
        if not email or not password or not password_again or not first_name or not last_name:
            messages.error(request, 'Please fill in all the information')
            return render(request,'html/register.html',content)

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
            last_name = last_name
        )

        account.save()
        print('created successfully!')
        messages.success(request, 'Register successfully')
        print(f'email:{email},password:{password}, password_again:{password_again},check_input:{check_input}')
        return redirect('register')

    return render(request, 'html/register.html')


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


def login_out(request):
    logout(request)
    return redirect('login')