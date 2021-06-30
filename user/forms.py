from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=32, help_text="only 32 symbols max")
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(widget=forms.EmailInput)
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
            self.add_error("username", "username exist")
        except User.DoesNotExist:
            return username

    def clean(self):
        super(UserRegistrationForm, self).clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            self.add_error("password1", "password does not match")
            self.add_error("password2", "password does not match")


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField
    fields = [
        "username",
        "lastname", "firstname",
        "email",
    ]

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name", "last_name",
            "password1", "password2"
        ]


class UserSignInForm(AuthenticationForm):
    pass
