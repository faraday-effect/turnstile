from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

from .forms import *

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print "GOT A FORM"
            pass
    else:
        form = LoginForm()
    return render(request, 'turnstile/login.html', { 'form': form })

def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['repeat_password']:
                messages.error(request, "Passwords didn't match")
            else:
                messages.success(request, "Account created")
                return redirect('turnstile_assignments')
    else:
        form = AccountForm()
    return render(request, 'turnstile/add_account.html', { 'form': form })

def assignments(request):
    return render(request, 'turnstile/assignments.html')

