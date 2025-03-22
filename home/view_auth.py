from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def login_view(request):
    if request.method=="POST":
        usn=request.POST.get("usn","").strip()
        password=request.POST.get("password","").strip()



        user =authenticate(request,username=usn,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Login Successful!")
            return redirect("home")
        else:
            messages.error(request,"Invalid usn or password.")
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect("intro")