from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html') 


def login_view(request):
    if request.method == 'POST':
        matricule = request.POST['matricule']
        password = request.POST['password']
        user = authenticate(request, username=matricule, password=password)
        print(matricule, password)

        if user is not None:
            login(request, user)
            return redirect('login:index')  # Replace 'home' with your desired redirect URL after login
        else:
            messages.error(request, 'Invalid matricule or password.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login:login')  # Replace 'login' with your desired redirect URL after logout
