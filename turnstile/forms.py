from django import forms

from .models import Student

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class AccountForm(forms.Form):
    full_name = forms.CharField(max_length=80)
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=20, widget=forms.PasswordInput())

    def clean_user_name(self):
        """Make sure no user with the same user_name."""
        user = self.cleaned_data.get("user_name")
        try:
            Student.objects.get(user_name=user)
        except Student.DoesNotExist:
            return user
        raise forms.ValidationError("Already a student with that user name")

    def clean_repeat_password(self):
        """Make sure the passwords match one another."""
        pass1 = self.cleaned_data.get("password")
        pass2 = self.cleaned_data.get("repeat_password")
        if pass1 != pass2:
            raise forms.ValidationError("Passwords don't match")
        return pass2
