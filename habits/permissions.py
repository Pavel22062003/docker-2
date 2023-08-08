from rest_framework.permissions import BasePermission


class HabitPermissions(BasePermission):
    message = 'Вы не являетесь автором привычки '

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
