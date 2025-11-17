from django.shortcuts import render

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def profile(request):
    return render(request, 'users/profile.html')

def email(request):
    return render(request, 'users/email.html')