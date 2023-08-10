
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


# Create your tests here.
class HabitTestcase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@yandex.ru'

        )
        self.user.set_password('1234')
        self.user.save()

        response = self.client.post(
            '/api/token/',
            {
                'email': 'test@yandex.ru',
                'password': '1234'
            }
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.habit = Habit.objects.create(
            user=self.user,
            place='место',
            time='10:00',
            action='действие',
            periodicity=1,
            reward='награда',
            time_to_complete='1:00'

        )

        self.second_habit = Habit.objects.create(
            place='место',
            time='10:00',
            action='действие',
            periodicity=1,
            reward='награда',
            time_to_complete='1:00'
        )

    def test_habit_delete(self):
        response = self.client.delete(
            '/habits/delete/5/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_habit_check_permissions(self):
        response = self.client.get(
            '/habits/detail/4/'

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_habit_list(self):
        response = self.client.get(
            '/habits/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_check_rules(self):
        response = self.client.post(
            '/habits/create/',

            place='место',
            time='10:00',
            action='действие',
            periodicity=1,
            reward='награда',
            time_to_complete='1:00',
            sign=True

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_habit_retrieve(self):
        response = self.client.get(
            '/habits/detail/9/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
