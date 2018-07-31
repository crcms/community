from django.db import models
from question.attributes import QuestionAttribute


# Create your models here.

class Question(models.Model):
    id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=120)
    content = models.TextField()
    user_id = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.SmallIntegerField(max_length=3, default=0, choices=tuple(
        zip(*[QuestionAttribute.get_transform('status').keys(), QuestionAttribute.get_transform('status').values()]))
                                      )
    good = models.IntegerField(default=0)
    bad = models.IntegerField(default=0)
    browse = models.IntegerField(default=0)
