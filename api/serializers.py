from rest_framework.serializers import ModelSerializer
from main import models

class OptionListSerializer(ModelSerializer):
    class Meta:
        model = models.Option
        fields = ['slug','name']


class QuestionListSerializer(ModelSerializer):
    options = OptionListSerializer(read_only=True, many=True)
    class Meta:
        model = models.Question
        fields = ['id','name', 'options']

class QuizDetailSerializer(ModelSerializer):
    questions = QuestionListSerializer(read_only=True, many=True)
    class Meta:
        model = models.Quiz
        fields = ['id', 'name', 'questions']

