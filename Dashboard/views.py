from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import DS
from .forms import new_reg_student_form,authuser
from django.contrib.auth.models import User
import re
def index(request):
    if request.method == "GET":
        return render(request,'index.html')

def reg_student(request):
    list_of_students = DS.objects.all()
    if request.method == "GET":
        return render(request,'dashboard.html',{"student":list_of_students})

def new_reg_student(request):
    if request.method == 'POST':
        forms = new_reg_student_form(request.POST)
        if forms.is_valid():
                forms.save()
    else:
        forms = new_reg_student_form()
    return render(request, 'new_reg_student.html', {"nrstform": forms})



def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            userdetail = DS.objects.filter(email_id=username)
            return render(request,'login_1st_page.html',{"student":userdetail})

        else:
            return HttpResponse("oops")
    else:
        return render(request,'registration/login.html')


def signup(request):
    if request.method == 'POST':
        forms = authuser(request.POST)
        password = request.POST['password']
        repassword= request.POST['repassword']
        if forms.is_valid() and password==repassword:
            forms.save()

            return redirect('login')
    else:
        forms = authuser()
    return render(request, 'registration/signup.html',{"signup": forms})