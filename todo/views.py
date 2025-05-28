from django.contrib.auth import logout,authenticate
from django.shortcuts import render, redirect


def dashboard(request):
    return render(request,"todo/dashboard.html")






