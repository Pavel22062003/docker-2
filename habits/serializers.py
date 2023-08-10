from rest_framework import serializers

from habits.models import Habit

from habits.validators import HabitValidator


class HabitBaseSerializer(serializers.ModelSerializer):
    validators = [HabitValidator()]

    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    validators = [HabitValidator()]

    class Meta:
        model = Habit

        fields = '__all__'
