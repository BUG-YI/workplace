import json

from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import *
@login_required(login_url='login')
def index(request):

    content = {'range_10': range(10)}

    return render(request, 'index.html', content)

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        f_name = data.get('f_name')
        l_name = data.get('l_name')
        email = data.get('email')
        password = data.get('password')
        a_password = data.get("a_password")
        agree = data.get('agree')
        username=f'{f_name}_{l_name}'
        content = {
            'f_name': f_name,
            'l_name': l_name,
            'email': email,
            'password': password,
            'a_password': a_password
        }

        if not all([f_name, l_name, email, password, a_password, ]):
            messages.error(request, 'Please fill in all the information!')
            return render(request, 'html/LR/register.html', content)

        if not agree:
            messages.error(request, 'Please check agree the agreement!')
            return render(request, 'html/LR/login.html', content)

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Account is exist!')
            return render(request, 'html/LR/register.html', content)

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is exist!')
            return render(request, 'html/LR/register.html', content)

        if password != a_password:
            messages.error(request, 'Please fill in twice different password!')
            return render(request, 'html/LR/register.html', {'f_name': f_name,
            'l_name': l_name,
            'email': email,})
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            account = Account(user=user, first_name=f_name, last_name=l_name)
            account.save()
            messages.success(request, 'Account created successfully, please login in!')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Network is busy!')
            return render(request, 'html/LR/register.html', content)

    return render(request, 'html/LR/register.html')
def login_page(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        agree = data.get('agree')

        content = {
            'email' : email
        }

        if not all([email, password, ]):
            messages.error(request, 'Please fill in all the information')
            return render(request, 'html/LR/login.html', content)

        if not agree:
            messages.error(request, 'Please check agree the agreement!')
            return render(request, 'html/LR/login.html', content)


        if not User.objects.exists():
            messages.error(request, 'Email or password is invalid!')
            return redirect('login')

        user = User.objects.get(email=email)
        account = authenticate(username=user.username, password=password)

        if account is None:
            messages.error(request, 'Email or password is invalid!')
            return redirect('login')
        else:
            login(request, account)
            return redirect('index')


    return render(request, 'html/LR/login.html')

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    messages.warning(request, 'Account logout!')
    return redirect('login')

@login_required(login_url='login')
def user_page(request):
    user = request.user
    username = user.username
    email = user.email
    f_name = user.account.first_name
    l_name = user.account.last_name
    gender = str(user.account.gender)
    gender_lis = ['Woman','Man', 'Unknown']
    tel = str(user.account.tel)
    if tel is None:
        tel = "Don't set telephone Number"
    f_add = user.account.family_address
    hobby = user.account.hobby
    user_picture = user.account.user_picture
    register_time = user.account.register_time

    contents = {
        'username': username,
        'email': email,
        'f_name': f_name,
        'l_name': l_name,
        'gender': gender,
        'tel': tel,
        'f_add': f_add,
        'hobby': hobby,
        # 'user_picture': user_picture,
        'register_time': register_time
    }

    if request.method == "POST":
        data = request.POST
        if data.get('change_information') == 'change_info':
            from utils.user_info import user_account_update_info
            keys = data.keys()
            key_dict = {}
            for k in keys:
                if k != 'change_information' and k != 'csrfmiddlewaretoken':
                    key_dict[k] = data.get(k)
            print(key_dict)
            update = user_account_update_info(key_dict)
            return JsonResponse(update)

        if data.get('picture_input') == 'uploadPicture' and request.FILES.get('user_picture'):
            from utils.user_info import user_account_update_user_picture
            result = user_account_update_user_picture(request)
            # print(request.FILES.get('user_picture'))
            # return None
            return JsonResponse(result)

    return render(request, 'html/User/user.html', context={'contents': contents, 'user_picture': user_picture})

@login_required(login_url='login')
def upload_flowers(request):
    contents = {
        'range_4': range(4)
    }

    if request.method == 'POST':
        data = request.POST
        print(data.keys())
        if data.get('form_upload_data') == 'from_upload_flower' and request.FILES.get('flower_pic'):
            from utils.flowers.flowers import upload_flowers
            d = {}
            for k in data.keys():
                d[k] = data.get(k)

            result = upload_flowers(request, d)

            return JsonResponse(result)

    if request.method == 'GET':
        from django.core import serializers
        objects_all = request.user.flowers.all().values('id', 'flower_name', 'flower_language','flower_growth_location','flower_information', 'flower_image')
        # print(objects_all)
        flower_lis = []
        for d in objects_all:
            flower_lis.append(d)

        print(flower_lis,)
        return render(request,'html/User/Part/uploadFlowers.html',{
            'flower_lis': flower_lis, #if len(flower_lis) != 0 else range(4)
            'count': -1
        })

    return render(request, 'html/User/Part/uploadFlowers.html', contents)