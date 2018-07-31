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
    status = models.SmallIntegerField(default=0, choices=tuple(
        zip(*[QuestionAttribute.get_transform('status').keys(), QuestionAttribute.get_transform('status').values()]))
                                      )
    good = models.IntegerField(default=0)
    bad = models.IntegerField(default=0)
    browse = models.IntegerField(default=0)

    def __str__(self):
        # return ''.join(['Id: ', str(self.id), ' ', 'Title: ' + self.title])
        # or
        # return 'Id: {id}, Title:{title}'.format(id=self.id, title=self.title)
        # or
        return 'Id: {0}, Title:{1}'.format(self.id, self.title)
