from django import forms
from django.core import validators

from .models import *

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())


class AccountForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    username = forms.CharField(max_length=20,
                               validators=[validators.validate_slug])
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=20, widget=forms.PasswordInput())

    def clean_username(self):
        """Make sure no user with the same username."""
        user = self.cleaned_data["username"]
        try:
            User.objects.get(username=user)
        except User.DoesNotExist:
            return user
        raise forms.ValidationError("Already a user with that user name")

    def clean_repeat_password(self):
        """Make sure the passwords match one another."""
        pass1 = self.cleaned_data["password"]
        pass2 = self.cleaned_data["repeat_password"]
        if pass1 != pass2:
            raise forms.ValidationError("Passwords don't match")
        return pass2


class SubmissionForm(forms.Form):
    file_name = forms.FileField()



class FeedbackForm(forms.ModelForm):
    def __init__(self, queryset, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['comments'] = forms.ModelMultipleChoiceField(queryset=queryset,
                                                                 widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Feedback
        fields = ('comments', 'extra_comment')
