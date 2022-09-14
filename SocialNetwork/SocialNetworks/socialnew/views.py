from django.shortcuts import render,redirect
from django.views.generic import View
from socialnew import forms
from django.contrib.auth.models import User

# Create your views here.

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        print(request.POST.get("username"))
        return render(request, "login.html")

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=forms.RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            print("Saved..")
        return redirect("signin")
