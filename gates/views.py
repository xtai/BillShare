from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Group, Record


@login_required
def index(request):
    context = {}
    return render(request, 'gates/index.html', context)


def signin(request):
    if request.method == 'POST':
        next_url = request.POST['next']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next_url == '':
                    next_url = '/'
                return redirect(next_url)
        return redirect('/login/')
    else:
        context = {}
        if 'next' in request.GET:
            context = {'next': request.GET['next']}
        return render(request, 'gates/login.html', context)


def logout(request):
    logout(request)
    return redirect('/login/')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    else:
        context = {}
        return render(request, 'gates/index.html', context)
