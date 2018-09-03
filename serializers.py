# -*- coding: utf-8 -*-

from rest_framework import serializers
from . import repositories
from .models import User

# from question import models
'''



'''


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = repositories.QuestionRepository().new_model().__class__
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'browse_num', 'good_num', 'comment_num')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'name', 'mobile', 'email')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = repositories.CategoryRepository().new_model().__class__
        fields = ('id', 'name', 'status', 'created_at', 'updated_at')
