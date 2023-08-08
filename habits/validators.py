from datetime import datetime, timedelta

from rest_framework import serializers

from habits.models import Habit


class HabitValidator:
    time_interval = timedelta(seconds=120)

    def __call__(self, value):
        if value.get('sign'):

            if value.get('connected_habit') or value.get('reward'):
                raise serializers.ValidationError(
                    'У приятной привычки не может быть вознаграждения или связанной привычки')

        if value.get('connected_habit'):
            # habit = Habit.objects.get(pk=value.get('connected_habit'))
            habit = value.get('connected_habit')

            if not habit.sign:
                raise serializers.ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки')

        if value.get('time_to_complete') > (datetime.min + self.time_interval).time():
            raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд')

        if value.get('connected_habit') and value.get('reward'):
            raise serializers.ValidationError(
                'Одновременный выбор связанной привычки и указания вознаграждения запрещён')
