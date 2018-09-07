from .models import Question, User, Category
from abc import ABCMeta, abstractmethod
from django.db.models import Model


class AbstractRepository(ABCMeta):

    @abstractmethod
    def new_model(self) -> Model:
        pass


class QuestionRepository(AbstractRepository):

    def new_model(self) -> Question:
        '''
        new model instance
        :return: Question
        '''
        return Question()

    def all(self):
        return Question.objects.all()


class UserRepository(AbstractRepository):
    def new_model(self) -> User:
        return User()


class CategoryRepository(AbstractRepository):
    def new_model(self) -> Category:
        return Category()
