from django.contrib import admin
from .models import Course, Prof, Enrollment


admin.site.register(Course)
admin.site.register(Prof)
admin.site.register(Enrollment)
