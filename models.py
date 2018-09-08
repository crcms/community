from django.db import models
from .attributes import QuestionAttribute
from time import time


class ModelSoftDeleteMixin(object):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = int(time())
        self.save()


# Create your models here.

class Question(ModelSoftDeleteMixin, models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    user_id = models.IntegerField(default=0)

    # def __init__(self):
    #     opts.concrete_fields

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


class User(models.Model):
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


class Category(ModelSoftDeleteMixin, models.Model):
    class Meta(object):
        db_table = 'community_categories'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.SmallIntegerField(default=0)

    def __init__(self, *args, **kwargs):

        # models.Model 初始化
        super(ModelSoftDeleteMixin, self).__init__(*args, **kwargs)

        self._meta.concrete_fields.append(self.created_at)
        self._meta.concrete_fields.append(self.updated_at)
        self._meta.concrete_fields.append(self.deleted_at)

        # self._meta.local_fields.append(2)
        # print(self._meta.local_fields)
