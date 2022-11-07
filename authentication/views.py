from django.shortcuts import render, redirect
# import HTTPResponse from django.http
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'login.html', {'message': 'Invalid Username or Password', 'title': 'Sign In - Report Card Commenter'})

    else:
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'login.html', {'message': '', 'title': 'Sign In - Report Card Commenter'})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'logout.html', {'title': 'Signing Out...'})

    else:
        return redirect('/auth')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_conf = request.POST.get('password-conf')

        if password != password_conf:
            return render(request, 'signup.html', {'message': 'Passwords do not match', 'title': 'Sign Up - Report Card Commenter'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'message': 'User already exists!', 'title': 'Sign Up - Report Card Commenter'})

        User.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'signup.html', {'message': 'Something went wrong, please try again later!', 'title': 'Sign Up - Report Card Commenter'})

    else:
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'signup.html', {'title': 'Sign Up - Report Card Commenter'})


def home(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        return redirect('/auth/login')
