from django.db import models
from .attributes import QuestionAttribute


# Create your models here.

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    user_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
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
    tel = models.CharField(max_length=15)
    status = models.SmallIntegerField(default=0)
    ticket = models.CharField(max_length=150)
    ticket_expired_at = models.BigIntegerField(default=0)
    deleted_at = models.BigIntegerField(null=True)
