from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    skills = models.CharField(max_length=20)
    hobbies = models.CharField(max_length=100,null=True,blank=True)