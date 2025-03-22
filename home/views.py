from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import Student
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home_view(request):
    
    user=request.user
    if not request.user.is_authenticated:
        return redirect("login") 
    try:
        student=Student.objects.get(email=user.email)
        attendance=student.attendance_count
    except Student.DoesNotExist:
        attendance=0
    context ={
        "attendance":attendance
    }

    return render(request,"home.html",context)
def student(request):
    return render(request,"student.html")
@login_required
def view_attendance(request):
    return render(request,"view_attendance.html")
def mark_attendance(request):
    return render(request,"mark_attendance.html")
def login(request):
    return render(request,"login.html")
def logout(request):
    return render(request,"logout.html")
def profile(request):
    return render(request,"profile.html")
def attendance(request):
    return render(request,"attendance_Records.html")
def register(request):
    if request.method=="POST":
        usn=request.POST["usn"]
        name=request.POST["name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1!=password2:
            messages.error("Passwords doesnt match")
            return redirect("register")
        
        if User.Objects.filter(username=usn).exists():
            messages.error("USN already exists")
            return redirect("register")
        
        if User.Objects.filter(email=email).exists():
            messages.error("Email already exists")
            return redirect("register")
        
        user=User.objects.create_user(username=usn,email=email,password=password1)
        user.first_name=name
        user.save()

        login(request,user)
        messages.success("Registered successfuly")
        redirect("home")
    return redirect(request,"register.html")

def intro(request):
    return render(request,"intro.html")

