# -*- coding: utf-8 -*-

from rest_framework import serializers
from question import models

# from question import models
'''



'''


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = models.Question
        fields = ('id', 'title', 'created_at', 'updated_at', 'browse_num', 'good_num', 'comment_num')
