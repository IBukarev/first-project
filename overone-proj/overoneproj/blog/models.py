from django.db import models

class Online(models.Model):
    name = models.CharField('Как тебя зовут', max_length=30)
    sms = models.TextField('Сообщение', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'