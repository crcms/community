# -*- coding: utf-8 -*-

'''

URL routes

'''

from django.urls import include,path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
