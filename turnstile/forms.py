from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class AccountForm(forms.Form):
    full_name = forms.CharField(max_length=80)
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=20, widget=forms.PasswordInput())

