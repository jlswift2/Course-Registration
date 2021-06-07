from django.shortcuts import render
import json
from .models import Course,Prof,Location


def home(request):
    return render(request, 'Home_Page/Home_Page.html', {})


def course_desc(request, course_number):
    course = Course.objects.get(number=course_number)
    return render(request, 'Course_Search/Course_Desc.html', {'course': course})


def course_search(request):
    data = {}
    if request.method == 'GET':
        courses = Course.objects.filter(name__icontains='course_name')
        data = {'courses': courses}

    return render(request, 'Course_Search/Course_Search.html', data)
