from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import serializers
from main import models


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def quizDetailView(request, id):
    quiz = models.Quiz.objects.get(id=id)
    serializer_data = serializers.QuizDetailSerializer(quiz)
    return Response(serializer_data.data)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def createQuizAnswer(request, id):
    try:
        quiz = models.Quiz.objects.get(id=id)
        start_time = request.data['start_time'],
        end_time = request.data['end_time']

        user = request.user
        answer = models.Answer.objects.create(
            quiz = quiz,
            author = user,
        )
        if start_time:
            answer.start_time = start_time
        if end_time:
            answer.end_time = end_time
        answer.save()

        for key, value in request.data.items():
            if key.isdigit():
                question = models.Question.objects.get(id=int(key))
                user_choice = models.Option.objects.get(slug=value)
                # assert question in quiz.questions and user_choice in question.options
                if question in quiz.questions and user_choice in question.options:
                    models.AnswerDetail.objects.create(
                        answer=answer,
                        question = question,
                        user_choice = user_choice
                    )
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)