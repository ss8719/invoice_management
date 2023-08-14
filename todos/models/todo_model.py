from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

from users_api.serializers import UserSerializer


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                           related_name="users_created_todos")


class TodoSerializer(serializers.ModelSerializer):
    created_by_user_id = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        # fields = ["title", "id"]
        fields = "__all__"
        # read_only_fields = ["title"]

    def to_representation(self, instance: Todo):
        # Get the default serialized data using the parent class method
        data = super(TodoSerializer, self).to_representation(instance)

        # Modify the value of the "name" field to "ram sing"
        # data["name"] = "ram sing"

        # data["created_by_user_id"] = UserSerializer(instance.created_by_user_id).data

        return data
    # def to_representation(self, instance):
    #     # Override the to_representation method to customize the response
    #     return {"id": instance.id, "created_by": UserSerializer(instance.created_by).data}
