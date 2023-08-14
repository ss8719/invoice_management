from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    assigned_to = models.ManyToManyField(User, related_name='tasks_assigned', )


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through="Enrollment")

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    final_grade = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = [['student', 'course']]
