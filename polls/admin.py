from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Course
admin.site.register(Student)
admin.site.register(Course)