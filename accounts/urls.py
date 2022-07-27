from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.user_dashboard, name='dashboard'),
    path('login', views.user_login, name='login'),
    path('register', views.user_register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('enroll_the_course', views.enroll_the_course, name='enroll_the_course'),


]
