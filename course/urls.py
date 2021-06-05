from django.urls import path
from . import views

urlpatterns = [
    path('course/<slug:course_number>/', views.course_desc, name='course_desc'),
    path('course/<)

]