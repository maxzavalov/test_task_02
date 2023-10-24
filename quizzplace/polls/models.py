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
