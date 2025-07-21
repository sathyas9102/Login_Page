from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Replace with your login URL name
        else:
            messages.error(request, 'Error in form submission.')
    else:
        form = UserCreationForm()
    return render(request, 'login_app/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_app/login.html', {'error': "Invalid credentials"})
    return render(request, 'login_app/login.html')

@login_required
def home_view(request):
    return render(request, 'login_app/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
