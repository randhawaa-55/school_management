# courses/models.py
from django.db import models
from students.models import Student
from teachers.models import Teacher

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
