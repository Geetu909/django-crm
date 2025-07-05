# dcrm/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, RecordForm
from .models import Record

def index(request):
    return render(request, 'dcrm/welcome.html')

@login_required
def home(request):
    records = Record.objects.all()  # Fetch all records
    return render(request, 'dcrm/index.html', {
        'username': request.user.username,
        'email': request.user.email,
        'last_login': request.user.last_login,
        'records': records,  # Pass records to the template
    })

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, 'Invalid login credentials')  # Set error message
    return render(request, 'dcrm/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully!')
    return redirect('index')  # Redirect to the index page after logout

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You have signed up successfully!')
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SignUpForm()
    return render(request, 'dcrm/signup.html', {'form': form})

@login_required
def add_record(request):
    form = RecordForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Record Added Successfully.")
        return redirect('home')  # Redirect to home after adding record
    return render(request, 'dcrm/add_record.html', {'form': form})
