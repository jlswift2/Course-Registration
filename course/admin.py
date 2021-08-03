from django.contrib import admin
from .models import Course, Enrollment, Student, Professor, Department

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Enrollment)
