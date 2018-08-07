from .models import Question,User


class QuestionRepository(object):

    def new_model(self) -> Question:
        '''
        new model instance
        :return: Question
        '''
        return Question()

    def all(self):
        return Question.objects.all()

class UserRepository(object):

    pass
