from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class': 'w-full py-2 px-2'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class': 'w-full py-2 px-2'
    }))

class SignupForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=('username', 'email','password1','password2')
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class': 'w-full py-2 px-2'
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email address',
        'class': 'w-full py-2 px-2'
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class': 'w-full py-2 px-2'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat password',
        'class': 'w-full py-2 px-2'
    }))
