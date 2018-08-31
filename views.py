from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.urls import reverse
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .repositories import QuestionRepository
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt
from crcms.settings import PASSPORT
from crcms.passports import Passport


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionRepository().all()
    serializer_class = QuestionSerializer


@csrf_exempt
def passport(request: HttpRequest):
    # print(type(request.body.decode()))
    # print(type(str(request.body,encoding='utf-8')))
    # print(request.body.decode(),123)
    print(request.POST)
    return JsonResponse({'a': '1'})


def index(request: HttpRequest):
    passport = Passport()
    result = passport.user(request.GET['token'])
    print('=====================')
    print(result['data'])
    print('=====================')
    return JsonResponse(result['data'])


def login(request: HttpRequest):
    host = 'http://' + PASSPORT['host']
    url = quote('http://127.0.0.1:28080' + reverse('community.index'))
    app_key = PASSPORT['key']

    return HttpResponse(
        bytes('<a href="' + host + '/login?_redirect=' + url + '&app_key=' + app_key + '">login</a>',
              encoding='UTF-8'))
