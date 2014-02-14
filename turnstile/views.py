from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

from .forms import *
from .models import *

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("user_name")
            try:
                student = Student.objects.get(user_name=user)
                if not check_password(form.cleaned_data.get("password"), student.password):
                    messages.error(request, "Wrong password")
                else:
                    return redirect('turnstile_assignments')
            except Student.DoesNotExist:
                messages.error(request, "That user name doesn't exist")
    else:
        form = LoginForm()
    return render(request, 'turnstile/login.html', { 'form': form })

def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            student = Student(full_name = form.cleaned_data.get("full_name"),
                              user_name = form.cleaned_data.get("user_name"),
                              password = make_password(form.cleaned_data.get("password")))
            student.save()
            messages.success(request, "Account created")
            return redirect('turnstile_assignments')
    else:
        form = AccountForm()
    return render(request, 'turnstile/add_account.html', { 'form': form })

def assignments(request):
    return render(request, 'turnstile/assignments.html')

