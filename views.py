from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from rest_framework import viewsets
from question.serializers import QuestionSerializer
from question.models import Question

# Create your views here.

def index(request: HttpRequest):
    return HttpResponse("hello")



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer