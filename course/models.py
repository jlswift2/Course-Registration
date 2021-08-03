from django.db import models
from django.conf import settings
import datetime

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gradyear = models.IntegerField()

    def __str__(self):
        return self.user.last_name + ', ' + self.user.first_name

class Professor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    bio = models.TextField()
    office_location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.last_name + ', ' + self.user.first_name


class Department(models.Model):
    department_key = models.CharField(max_length=4)

class Course(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=200)
    days = models.CharField(max_length=200)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    prof = models.ForeignKey(
        'Professor', on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Enrollment')

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=datetime.datetime.now())
    final_grade = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = [['student', 'course']]
