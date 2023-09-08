from django.shortcuts import render
from .models import User

# Create your views here.

def home(request):
    return render(request,'intro/home.html')

def register(request):
    return render(request,'intro/register.html')

def login (request):
    new_user = User()
    new_user.username = request.POST.get('username')
    new_user.password = request.POST.get('password')
    new_user.save()

    accounts = {
        'accounts':User.objects.all()
    }
    return render(request, 'intro/login.html',accounts)