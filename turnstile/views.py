from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

from .forms import *
from .models import *

def login(request):
    """Log in a student."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data["user_name"],
                                     password=form.cleaned_data["password"])
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Login successful")
                return redirect('turnstile_assignments')
            else:
                messages.error(request, "Invalid login; try again")
    else:
        form = LoginForm()
    return render(request, 'turnstile/login.html', { 'form': form })

def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out")
    return redirect('turnstile_login')

def add_account(request):
    """Add a student account."""
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            student = User.objects.create_user(form.cleaned_data["username"],
                                               form.cleaned_data["email"],
                                               form.cleaned_data["password"])
            student.first_name = form.cleaned_data["first_name"]
            student.last_name = form.cleaned_data["last_name"]
            student.save()

            try:
                student_group = Group.objects.get(name='Student')
                student.groups.add(student_group)
                messages.success(request, "Account created")
            except Group.DoesNotExist:
                messages.error(request, "Couldn't add new student to group")

            return redirect('turnstile_login')
    else:
        form = AccountForm()
    return render(request, 'turnstile/add_account.html', { 'form': form })

@login_required
def assignments(request):
    all_hw = Assignment.objects.all()
    return render(request, 'turnstile/assignments.html', { 'all_hw': all_hw })

@login_required
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
                print type(request.user), request.user
                Submission.objects.create(student=request.user,
                                          assignment=assignment,
                                          submitted_file=form.cleaned_data['file_name'])
                messages.success(request, "Homework submitted")
            except User.DoesNotExist:
                message.error("Can't find current student")
    else:
        form = SubmissionForm()

    return render(request, 'turnstile/submission.html',
                  { 'form': form,
                    'assignment': assignment,
                    'submissions': submissions })

@login_required
def delete_submission(request, submission_id):
    try:
        submission = Submission.objects.get(pk=submission_id)
        assignment = submission.assignment
        submission.submitted_file.delete(save=False)
        submission.delete()
        messages.success(request, "Submission deleted")
        return redirect('turnstile_submit', assignment_id=assignment.pk)
    except Submission.DoesNotExist:
        messages.error(request, "Can't find submission")
        return redirect('turnstile_assignments')

@permission_required('turnstile.view_submissions', raise_exception=True)
def list_submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'turnstile/submissions.html', { 'submissions': submissions })

def handle_403(request):
    return render(request, 'turnstile/403-forbidden.html')

def handle_404(request):
    return render(request, 'turnstile/404-not-found.html')

def handle_500(request):
    return render(request, 'turnstile/500-internal-server-error.html')
