from django.shortcuts import render
from django.http import HttpRequest,JsonResponse,HttpResponse
from django.urls import reverse
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .repositories import QuestionRepository
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionRepository().all()
    serializer_class = QuestionSerializer

@csrf_exempt
def passport(request: HttpRequest):
    # print(type(request.body.decode()))
    # print(type(str(request.body,encoding='utf-8')))
    # print(request.body.decode(),123)
    print(request.POST)
    return JsonResponse({'a':'1'})

def index(request):
    return HttpResponse('Index')

def login(request: HttpRequest):

    url = quote('http://192.168.1.142:28080'+reverse('community.index'))

    return HttpResponse(bytes('<a href="http://laravel.test/login?_redirect='+url+'">login</a>',encoding='UTF-8'))

