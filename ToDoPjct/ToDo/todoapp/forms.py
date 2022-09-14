from django import forms
from django.contrib.auth.models import User

# class RegistrationForm(forms.Form):
#     first_name=forms.CharField()
#     last_name=forms.CharField()
#     username=forms.CharField()
#     email=forms.EmailField()
#     password=forms.CharField()   or

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "email",
            "username",
            "password"
        ]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()