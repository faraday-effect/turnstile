from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

from .forms import *
from .models import *

def login(request):
    """Log in a student."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Make sure the student exists.
            user = form.cleaned_data["user_name"]
            try:
                student = Student.objects.get(user_name=user)
                # Check the password.
                if not check_password(form.cleaned_data["password"], student.password):
                    messages.error(request, "Wrong password")
                else:
                    # Log in the student.
                    request.session['student_id'] = student.id
                    return redirect('turnstile_assignments')
            except Student.DoesNotExist:
                messages.error(request, "That user name doesn't exist")
    else:
        form = LoginForm()
    return render(request, 'turnstile/login.html', { 'form': form })

def add_account(request):
    """Add a student account."""
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            student = Student(full_name = form.cleaned_data["full_name"],
                              user_name = form.cleaned_data["user_name"],
                              password = make_password(form.cleaned_data["password"]))
            student.save()
            messages.success(request, "Account created")
            return redirect('turnstile_assignments')
    else:
        form = AccountForm()
    return render(request, 'turnstile/add_account.html', { 'form': form })

def assignments(request):
    all_hw = Assignment.objects.all()
    return render(request, 'turnstile/assignments.html', { 'all_hw': all_hw })

def submit(request, assignment_id):
    try:
        assignment = Assignment.objects.get(pk=assignment_id)
    except Assignment.DoesNotExist:
        messages.error("Can't find selected assignment")
        return redirect('turnstile_assignments')

    submissions = Submission.objects.filter(assignment=assignment)

    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
                try:
                    student = Student.objects.get(pk=request.session['student_id'])
                    submission = Submission(student=student,
                                            assignment=assignment,
                                            submission=form.cleaned_data['file_name'])
                    submission.save()
                    messages.success(request, "Homework submitted")
                except Student.DoesNotExist:
                    message.error("Can't find current student")
    else:
        form = SubmissionForm()

    return render(request, 'turnstile/submission.html',
                  { 'form': form,
                    'submissions': submissions })

def delete_submission(request, submission_id):
    try:
        submission = Submission.objects.get(pk=submission_id)
        assignment = submission.assignment
        submission.submission.delete(save=False)
        submission.delete()
        messages.success(request, "Submission deleted")
        return redirect('turnstile_submit', assignment_id=assignment.pk)
    except Submission.DoesNotExist:
        messages.error(request, "Can't find submission")
        return redirect('turnstile_assignments')


