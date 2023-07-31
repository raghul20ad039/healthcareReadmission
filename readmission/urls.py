from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("appointment",views.appointment,name="appointment"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("services",views.services,name="services"),
    path("dashboard",views.dashboard,name="dashboard"),
]
