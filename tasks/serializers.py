# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task, TaskAssignment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    assigned_to = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_name(self, obj):
        return "dkljafl"

    def get_assigned_to(self, obj):
        ta = obj.task_assignments.all()
        return [assignment.user.id for assignment in ta]


class TaskAssignmentSerializer(serializers.ModelSerializer):
    assigned_by = UserSerializer(read_only=True)
    task = TaskSerializer()

    class Meta:
        model = TaskAssignment
        fields = ['assigned_by', "task"]
