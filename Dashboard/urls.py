from django.urls import path
from . import views
#login default django
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index),
    path('re/', views.reg_student, name='rstudent'),
    path('new_reg_student/',views.new_reg_student,name="nrstudent"),
    path('log/',views.login_,name='login'),
    path('signup/',views.signup,name='signup')
]