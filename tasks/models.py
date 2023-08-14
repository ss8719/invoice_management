# Create your models here.
# todo_assign_model.py
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.title


class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_assignments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_by_tasks')
    assigned_at = models.DateTimeField(auto_now_add=True)
