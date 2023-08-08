from django.core.management import BaseCommand
import telebot

from config import settings
from users.models import User


class Command(BaseCommand):
    """Ручная команда для запуска бота"""

    def handle(self, *args, **options):
        token = settings.TELEGRAM_API_TOKEN
        bot = telebot.TeleBot(token)

        @bot.message_handler(commands=['start'])
        def start_welcome(message):

            try:
                user_chat_id = User.objects.get(tg_chat_id=message.chat.id)

                bot.send_message(message.chat.id, 'Привет, ваш телеграм уже подключен к сайту')


            except:

                bot.send_message(message.chat.id,
                                 'Привет, ваш телеграм ещё не подключен, для того чтобы получать привычки, пожалуйста отправьте ваш email , с которым вы регистрировались на сайте')

        @bot.message_handler(func=lambda message: True)
        def check(message):
            try:
                user = User.objects.get(email=message.text)
                user.tg_chat_id = message.chat.id
                user.save()

                bot.send_message(message.chat.id, 'Спасибо, ваш телеграм успешно подключён ')
            except:
                bot.send_message(message.chat.id,
                                 'Что то пошло не так , пожалуйста проверьте корректность отправляемой почты')

        bot.infinity_polling()
