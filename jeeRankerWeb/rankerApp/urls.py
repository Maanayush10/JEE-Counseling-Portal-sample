from django.urls import path, include
from rankerApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("newUser", views.signUp, name='SignUp'),
    path("login", views.loginUser, name='loginUser'),
    path("logout", views.logoutUser, name='logoutUser'),
    path("dashboard", views.dashboard, name="dashboard"),
    path("results", views.results, name="results"),
]
