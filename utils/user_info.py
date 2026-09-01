import os
import time

from django.contrib.auth.models import User

from home.models import Account

from typing import Any

def user_account_update_info(d_dict: dict[str,Any]):
    """
    更新Account模型数据
    :param d_dict: 数据字典
    :return:
    """
    user = User.objects.get(email=d_dict['email'])
    user.username = f"{d_dict['f_name']}_{d_dict['l_name']}"
    user.save()
    Account.objects.update_or_create(
        user=user,
        defaults = {
            'first_name': d_dict['f_name'],
            'last_name': d_dict['l_name'],
            'tel': int(d_dict['tel']),
            'gender': int(d_dict['gender']),
            'hobby': d_dict['hobby'],
            'family_address': d_dict['f_add']
        }
    )
    return {
        'status': 200,
        'msg': 'Success updated, please refresh page!'
    }

def user_account_update_user_picture(request, ):
    try:
        old_picture = request.user.account.user_picture
        # print("old:",old_picture)
        user = request.user
        Account.objects.update_or_create(
            user=user,
            defaults={
                'user_picture': request.FILES.get('user_picture')
            }
        )
        if os.path.isfile(old_picture.path):
            os.remove(old_picture.path)
    except Exception as e:
        print(f'account upload failed :{e}')
        return {
            'status': 404,
            'msg': f'Upload failed'
        }

    return {
        'status': 200,
        'msg': 'Upload success'
    }