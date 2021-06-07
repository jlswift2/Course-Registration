from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course_search, name='course_search'),
    path('course/<slug:course_number>/', views.course_desc, name='course_desc'),
]
