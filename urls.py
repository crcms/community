# -*- coding: utf-8 -*-

'''

URL routes

'''

from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('passport', views.passport, name='community.passport'),
    path('login', views.login, name='community.login'),
    path('index', views.index,name='community.index')
]
