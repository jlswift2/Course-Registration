from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    days = models.CharField(max_length=200)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    prof = models.ForeignKey(
        'Prof', on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Prof(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    office_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# class Location(models.Model):
#     building = models.CharField(max_length=200)
#     address = models.TextField()
#     room_number = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.building + self.room_number

#class User(AbstractUser):
 #   is_student = models.BooleanField()
  #  is_teacher = models.BooleanField()
