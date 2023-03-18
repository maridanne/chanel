from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *
from userprofile.models import User
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import MultipleObjectsReturned

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            messages.info(request, 'Username or password is incorrect.')
            

    return render(request, 'userprofile/login.html')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('user_login')

    context = {'form': form}
    return render(request, 'userprofile/signup.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

