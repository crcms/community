from django.db import models
from .attributes import QuestionAttribute
from abc import ABCMeta
from time import time


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = int(time())
        self.save()


# Create your models here.

class Question(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    user_id = models.IntegerField(default=0)

    status = models.SmallIntegerField(default=0, choices=tuple(
        zip(*[QuestionAttribute.get_transform('status').keys(), QuestionAttribute.get_transform('status').values()]))
                                      )
    good_num = models.IntegerField(default=0, editable=False)
    comment_num = models.IntegerField(default=0, editable=False)
    browse_num = models.IntegerField(default=0, editable=False)

    def __str__(self):
        # return ''.join(['Id: ', str(self.id), ' ', 'Title: ' + self.title])
        # or
        # return 'Id: {id}, Title:{title}'.format(id=self.id, title=self.title)
        # or
        return 'Id: {0}, Title:{1}'.format(self.id, self.title)


class User(BaseModel):
    class Meta(object):
        db_table = 'users'
        managed = False

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15)
    status = models.SmallIntegerField(default=0, choices=tuple(
        zip(*[QuestionAttribute.get_transform('status').keys(), QuestionAttribute.get_transform('status').values()])))
    deleted_at = models.BigIntegerField(null=True)


class Category(BaseModel):
    class Meta(object):
        db_table = 'community_categories'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.SmallIntegerField(default=0)
