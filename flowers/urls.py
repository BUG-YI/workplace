from django.urls import path

from .views import *

urlpatterns = [
    path('', f_index, name='f_index'),
    # path('User/', )
]