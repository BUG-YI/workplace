from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null=True, blank=True)

    first_name = models.CharField()
    last_name = models.CharField()