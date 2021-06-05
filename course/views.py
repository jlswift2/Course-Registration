from django.shortcuts import render
import json
from .models import Course,Prof,Location

# def course_desc(request, course_number):
#     course = Course.objects.get(number=course_number)
#     return render(request, 'Course_Search/Course_Desc.html', {'course': course})
#
# def course_list(request, course_name):
#     courses = Course.objects.filter(name__icontains=course_name)
#     return render(request, 'Course_Search/Course_List.html', courses)
