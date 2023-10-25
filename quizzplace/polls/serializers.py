from rest_framework import serializers
from .models import Answer, Question, Poll


class AnswerSerializer(serializers.ModelSerializer):
    """Сериализатор данных для модели ответа."""

    class Meta:
        model = Answer
        fields = ["text", "isCorrect"]


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор данных для модели вопроса."""

    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ["text", "type", "answers"]


class PollSerializer(serializers.ModelSerializer):
    """Сериализатор данных для модели опроса."""

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ["name", "dateFrom", "dateTo", "isActive", "questions"]
