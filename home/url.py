from django.contrib import admin
from django.urls import path,include
from home import views
from .view_auth import login_view,logout_view
urlpatterns = [
    path("",views.intro,name="intro"),
    path("home/",views.home_view,name="home"),
    path("students/",views.student,name="student"),
    path("attendance/view/",views.view_attendance,name="view_attendance"),
    path("attendance/mark/",views.mark_attendance,name="mark_attendance"),
    path("logout",logout_view,name="logout"),
    path("profile/",views.profile,name="profile"),
    path("attendance/",views.attendance,name="attendance"),
    path("register/",views.register,name="register"),
    path("login/",login_view,name='login')
]
