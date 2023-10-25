from django.db import models


class Poll(models.Model):
    """Модель опроса."""


    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название опроса")
    dateFrom = models.DateTimeField(null=False, blank=False, editable=False, verbose_name="Дата начала опроса")
    dateTo = models.DateTimeField(null=False, blank=False, editable=False, verbose_name="Дата окончания опроса")
    isActive = models.BooleanField(default=True, verbose_name="Статус опроса")

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Question(models.Model):
    """Модель вопроса."""

    QUESTIONS_TYPES = [("text input", "Text input"), ("answer choice", "Answer choice")]

    text = models.CharField(max_length=300, null=False, blank=True, verbose_name="Текст вопроса")
    type = models.CharField(max_length=50, choices=QUESTIONS_TYPES, verbose_name="Тип вопроса")
    survey = models.ForeignKey(Poll, related_name='question', on_delete=models.CASCADE, verbose_name="Опрос")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    """Модель ответа."""

    text = models.TextField(max_length=1500, null=False, blank=True, verbose_name="Текст ответа")
    isCorrect = models.BooleanField(verbose_name="Является ли ответ верным")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer', verbose_name='Вопрос')

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"