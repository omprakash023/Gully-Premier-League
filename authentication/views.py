from django.shortcuts import render, redirect
from django.contrib.auth.models import auth


# Create your views here.

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
