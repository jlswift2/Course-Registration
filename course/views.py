from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EnrollmentForm
from .models import Course, Student, Professor, Enrollment, Department
import datetime

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return redirect(home)
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'registration/login.html', {"invalid": 'invalid'})
    else:
        # No post data available, let's just show the page to the user.
        return render(request, 'registration/login.html')

@login_required
def home(request):
    if request.user.is_staff:
        return render(request, 'Home_Page/Home_Page_Staff.html', {})
    else:
        return render(request, 'Home_Page/Home_Page.html', {})


@login_required
def account_dashboard(request):
    return render(request, 'user_dashboard/user_dashboard.html', {})

@login_required
def my_classes(request):
    enrollments = Enrollment.objects.filter(student__username__iexact=request.user.username)
    data = {}
    if enrollments:
        data = {'schedule': enrollments}
    else:
        data['empty'] = 'empty'
    return render(request, 'user_dashboard/user_schedule.html', data)

@login_required
def unenroll(request, pk):
    course = Enrollment.objects.get(id=pk)
    data = {'course': course}
    if request.method == 'POST':
        course.delete()
        return redirect('/')
    return render(request, 'user_dashboard/delete.html', data)


@login_required
def course_desc(request, pk):
    course = Course.objects.get(pk=pk)
    data = {'course': course}
    if request.method == 'POST':
        enroll = EnrollmentForm(request.POST or None)
        if enroll.is_valid():
            try:
                enrollment = enroll.save(commit=False)
                enrollment.student = request.user
                enrollment.course = course
                enrollment.date_enrolled = datetime.datetime.now()
                enrollment.save()
                return render(request, 'Course_Search/Course_Desc.html', data)
            except IntegrityError:
                data['unique'] = 'unique'
            return render(request, 'Course_Search/Course_Desc.html', data)
    else:
        return render(request, 'Course_Search/Course_Desc.html', data)

@login_required
def course_search(request):
    data = {}
    really = False
    if request.method == 'GET' and 'name' in request.GET.keys():
        really = True
        courses = Course.objects.filter(name__icontains=request.GET.get('name'))
        data['courses'] = courses
    data['really'] = really
    return render(request, 'Course_Search/Course_Search.html', data)

@login_required
def course_browse_base(request):
    data = {}
    departments = Department.objects.all()
    data['departments'] = departments
    print(data)
    return render(request, 'Course_Search/Course_Browse.html', data)

@login_required
def course_browse_department(request, department_key):
    department = Department.objects.get(department_key=department_key)
    courses = Course.objects.filter(department__department_key__icontains=department.department_key)
    data = {'courses': courses}
    print(data)
    return render(request, 'Course_Search/Course_Browse_Department.html', data)

@login_required
def prof_bio(request, pk):
    prof = Professor.objects.get(pk=pk)
    data = {'prof': prof}
    print(data)
    return render(request, 'prof_info/prof_bio.html', data)
