from django.contrib import admin
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
        path('login',views.login,name="login"),
        path('',views.home,name="home"),
        path('logout',views.logout,name="logout"),
        path('register',views.register,name="register"),

]