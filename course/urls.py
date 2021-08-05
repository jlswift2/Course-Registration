from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('course/', views.course_search, name='course_search'),
    path('course/browse', views.course_browse_base, name='course_browse'),
    path('course/browse/<slug:department_key>', views.course_browse_department, name='course_department'),
    path('course/<int:pk>/', views.course_desc, name='course_desc'),
    path('prof/<int:pk>/', views.prof_bio, name='prof_bio'),
    path('user/<slug:user.username>/', views.account_dashboard, name='account_dashboard')
]
