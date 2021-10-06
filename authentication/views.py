from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SignUpForm

# Create your views here.


def index(request):
    return render(request,'index.html')


@csrf_exempt
def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', context={'form': form})
