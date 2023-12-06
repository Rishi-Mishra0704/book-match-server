from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fiction_score = models.FloatField()
    non_fiction_score = models.FloatField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    fiction_score = models.FloatField()
    non_fiction_score = models.FloatField()
