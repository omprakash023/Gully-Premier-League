from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import re
# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if re.search('[A-Z]', password1) == None and re.search('[0-9]', password1) == None and re.search('[^A-Za-z0-9]', password1) == None and re.search('[[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]]', password1)==None:
                messages.info(request, 'Password must contain  one Capital,numeric and symbol characters')
                return redirect('signup')
            elif len(password1) < 8:
                messages.info(request, "Password must contains 8 characters")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Account registered for "+ username)
        else:
            messages.info(request,"Password not matching")
            return redirect('signup')
        return redirect('/')

    else:
        return render(request,'index.html')

