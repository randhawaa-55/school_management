# teachers/models.py
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=10, unique=True)
