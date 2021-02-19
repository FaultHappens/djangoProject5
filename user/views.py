from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import UserManager
# Create your views here.

def register(request):
    context = {}
    email = request.POST["email"]
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    tel = request.POST["tel"]
    password = request.POST["password"]

    UserManager.create_user(email, tel, lname, fname, password)
    return render(request, 'user/register.html', context)

def login(request):
    context = {}

    return render(request, 'user/login.html', context)
