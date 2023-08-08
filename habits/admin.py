from django.contrib import admin

from habits.models import Habit


# Register your models here.
@admin.register(Habit)
class AdminHabit(admin.ModelAdmin):
    list_display = ['user', 'action']
