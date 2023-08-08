from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import HabitPermissions
from habits.serializers import HabitBaseSerializer, HabitCreateSerializer


# Create your views here.


class HabitsListApiView(generics.ListAPIView):
    pagination_class = HabitPaginator
    queryset = Habit.objects.all()
    serializer_class = HabitBaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Выдача пользователю публичных привычек и его собственных"""
        user = self.request.user
        queryset = Habit.objects.filter(publicity=True) | Habit.objects.filter(user=user)

        return queryset


class HabitsCreateApiView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDetailApiView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitBaseSerializer
    permission_classes = [HabitPermissions]


class HabitUpdateApiView(generics.UpdateAPIView):

    queryset = Habit.objects.all()
    serializer_class = HabitBaseSerializer
    permission_classes = [HabitPermissions]


class HabitDeleteApiView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitBaseSerializer
    permission_classes = [HabitPermissions]

