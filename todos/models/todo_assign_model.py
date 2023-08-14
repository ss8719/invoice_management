from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

from todos.models.todo_model import Todo
from users_api.serializers import UserSerializer


class TodoAssign(models.Model):
    todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE, )
    assigned_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                            related_name='assigned_by_user', editable=False)
    assigned_to_user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                            related_name='assigned_to_user')
    assigned_at = models.DateTimeField(auto_now=True)


class TodoAssignSerializer(serializers.ModelSerializer):
    assigned_by_user_id = UserSerializer(read_only=True)

    class Meta:
        model = TodoAssign
        fields = '__all__'
