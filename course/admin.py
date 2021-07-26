from django.contrib import admin
from .models import Course, Prof, Enrollment, Student, Professor

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Enrollment)
