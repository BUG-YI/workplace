from django.db import models

from django.contrib.auth.models import User

from utils.models.Rename import PictureRename

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tel = models.IntegerField(default=0)
    gender_choices = [(0, 'woman'), (1, 'man'), (2, 'unknown')]
    gender = models.IntegerField(choices=gender_choices, default=2)
    hobby = models.TextField(blank=True, default='还未设置爱好')
    family_address = models.TextField(blank=True, default='暂居地球村')
    user_picture = models.ImageField(upload_to=PictureRename('user_picture/'), blank=True, null=True, default='default/user_default.png')

    register_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # last_login = models.DateTimeField(auto_now=True)