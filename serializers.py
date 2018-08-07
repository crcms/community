# -*- coding: utf-8 -*-

from rest_framework import serializers
from . import repositories

# from question import models
'''



'''


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = repositories.QuestionRepository().new_model().__class__
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'browse_num', 'good_num', 'comment_num')
