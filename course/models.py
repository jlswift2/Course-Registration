from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime



class Student(User):
    gradyear = models.IntegerField()

    def __str__(self):
        return self.name

# class Professor(ContactInfo):
#     department = models.CharField(max_length=200)
#     lkasjd
#     bio = models.TextField()

# class staff:
#     ;lkas
#     lkasjd
#     lkasjdf
#

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
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Enrollment')

    def __str__(self):
        return self.name

class Prof(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    office_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=datetime.datetime.now())
    final_grade = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = [['student', 'course']]
