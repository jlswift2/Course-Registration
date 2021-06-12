from django.shortcuts import render
import json
from .models import Course,Prof,Location


def home(request):
    return render(request, 'Home_Page/Home_Page.html', {})


def course_desc(request, pk):
    course = Course.objects.get(pk=pk)
    data = {'course': course}
    print(data)
    return render(request, 'Course_Search/Course_Desc.html', data)


def course_search(request):
    data = {}
    really = False
    if request.method == 'GET' and 'name' in request.GET.keys():
        really = True
        courses = Course.objects.filter(name__icontains=request.GET.get('name'))
        data['courses'] = courses
    data['really'] = really
    return render(request, 'Course_Search/Course_Search.html', data)
