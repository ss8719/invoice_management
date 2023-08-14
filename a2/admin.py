from django.contrib import admin

from a2.models import Student, Course, Enrollment

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
