from django.shortcuts import render,redirect
from . forms import UserLogin,UserRegister
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from courses.models import Course
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/accounts/login')
def user_dashboard(request):
    current_user = request.user
    courses = current_user.courses.all()
    context = {
        'courses':courses
    }
    return render(request,'dashboard.html',context)


def user_login(request):
    form = UserLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request,username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                messages.warning(request,'Sizin hesab bloklanmışdır!')
        else:
            messages.warning(request,'Səhf logn və ya şifrə')


    context = {
        'form':form,
    }
    return render(request,'login.html',context)


def user_register(request):
    form = UserRegister(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Qeydiyyat uğurla bitdi')
        return redirect('login')
    context = {
        'form':form,
    }
    return render(request,'register.html',context)


def user_logout(request):
    logout(request)
    return redirect('index')


def enroll_the_course(request):
    course_id = request.POST['course_id']
    user_id = request.POST['user_id']
    course = Course.objects.get(id = course_id)
    user = User.objects.get(id = user_id)
    course.students.add(user)
    return redirect('dashboard')