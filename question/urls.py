# -*- coding: utf-8 -*-

'''

URL routes

'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
