from django.urls import path
from socialnew import views

urlpatterns=[
    path("login",views.LoginView.as_view(),name="login"),
    path("register",views.SignUpView.as_view(),name="signin")
]

# New Project ToDo>todoapp
# todo Models> create new model Todos inside todoapp Models with fields taskname,user,status,date