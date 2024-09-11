from . import models


def create_datas():
    q1 = models.Quiz.objects.create(name=1)
    q2 = models.Quiz.objects.create(name=2)
    models.Quiz.objects.create(name=3)
    models.Quiz.objects.create(name=4)

    models.Question.objects.create(quiz=q1, name='a')