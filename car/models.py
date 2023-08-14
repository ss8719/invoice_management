from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Showroom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="show_room_created_by_user")
    email = models.EmailField(null=True)


class ShowroomDetails(models.Model):
    owner_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    show_room = models.OneToOneField(Showroom, on_delete=models.CASCADE, related_name="show_room_details")


class Car(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="car_created_by_user", editable=False)
    show_room = models.ForeignKey(Showroom, on_delete=models.CASCADE, related_name="showroom_all_cars")
