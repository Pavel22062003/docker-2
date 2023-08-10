from datetime import datetime, timedelta

from celery import shared_task

from config import settings
from habits.models import Habit
from users.models import User
import telebot


@shared_task
def check_task():
    token = settings.TELEGRAM_API_TOKEN
    bot = telebot.TeleBot(token)
    now = datetime.now().time()  # Текущее время
    users = User.objects.filter(tg_chat_id__isnull=False)

    for user in users:

        # Получить все записи привычек, где поле 'время' меньше или равно текущему времени
        habits_to_complete = Habit.objects.filter(time__lte=now, user=user)

        for habit in habits_to_complete:
            habit_time = habit.time

            # Получить периодичность привычки
            frequency = habit.periodicity
            # Определить интервал в зависимости от периодичности
            if frequency == '1':
                interval = timedelta(days=1)
            elif frequency == '2':
                interval = timedelta(days=2)
            elif frequency == '3':
                interval = timedelta(days=3)
            else:
                continue

            current_time = datetime.combine(datetime.today(), now)
            habit_datetime = datetime.combine(datetime.today(), habit_time)

            # Разница между текущим временем и временем привычки
            time_difference = current_time - habit_datetime

            # Проверить, наступило ли время выполнения привычки с учетом переодичности
            if time_difference.total_seconds() >= 0 and time_difference.total_seconds() % interval.total_seconds() == 0:
                message = f"Пора выполнить привычку: {habit.action}"
                bot.send_message(user.tg_chat_id, message)
