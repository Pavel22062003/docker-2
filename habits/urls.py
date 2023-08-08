from habits.views import HabitsListApiView, HabitsCreateApiView, HabitDetailApiView, HabitUpdateApiView, \
    HabitDeleteApiView
from django.urls import path

urlpatterns = [
    path('', HabitsListApiView.as_view()),
    path('create/', HabitsCreateApiView.as_view()),
    path('detail/<int:pk>/', HabitDetailApiView.as_view()),
    path('update/<int:pk>/', HabitUpdateApiView.as_view()),
    path('delete/<int:pk>/', HabitDeleteApiView.as_view())


]