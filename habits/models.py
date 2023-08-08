from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Habit(models.Model):
    periodicity_choices = (
        (1, 'everyday'),
        (2, 'twice a week'),
        (3, 'thrice a week'),

    )

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)
    place = models.CharField(verbose_name='место в котором нужно выполнить привычку')
    time = models.TimeField(verbose_name='время, когда необходимо выполнять привычку')
    action = models.CharField(verbose_name='действие, которое нужно выполнить')
    sign = models.BooleanField(verbose_name='признак приятной привычки', default=False)
    connected_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE)
    periodicity = models.IntegerField(choices=periodicity_choices, verbose_name='периодичность')
    reward = models.CharField(verbose_name='награда', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='время на выполнение')
    publicity = models.BooleanField(default=True, verbose_name='признак публичности')
