from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models



class SignUp (UserCreationForm):
    email = forms.EmailField(required=True)
    class  Meta:
        model= User
        fields=('first_name', 'last_name','email','username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
