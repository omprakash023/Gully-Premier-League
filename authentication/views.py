from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .backends import EmailBackend


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = EmailBackend.authenticate(email, password)
        if user is not None:
            login(request, user)
            messages.success(
                request, " Successfully Logged In.")
            return redirect('home')

        else:
            messages.error(
                request, " Invalid credintials, Please try again.")
            return redirect('/')


def home(request):
    return render(request, 'dashboard.html')
