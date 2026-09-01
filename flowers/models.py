from django.db import models
from django.contrib.auth.models import User

from utils.models.Rename import PictureRename

class Flowers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flowers')
    flower_name = models.CharField(max_length=30)
    flower_language = models.CharField(max_length=100, blank=True, default='')
    flower_growth_location = models.CharField(max_length=20, blank=True, default='')
    flower_information = models.TextField(blank=True, default='')
    flower_image = models.ImageField(upload_to=PictureRename('flowers/'))

    flower_register_time = models.DateTimeField(auto_now_add=True)
    flower_change_time = models.DateTimeField(auto_now=True)