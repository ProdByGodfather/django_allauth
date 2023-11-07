from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


@login_required
def home(request):
    context = {

    }
    return render(request,'home.html',context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = authenticate(username=username,password=password)
        if u:
            login(request,u)
            return redirect('home')
        else:
            error = 'your user or password does not exists'
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')