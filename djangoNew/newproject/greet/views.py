from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

# Create your views here.

class GoodMorningView(APIView):
    def get(self,respons,*args,**kwars):
        return Response({"msg":"good morning....."})

class GoodEveningView(APIView):
    def get(self,respons,*args,**kwargs):
        return Response({"msg":"Good evening all...."})

class Greetings(APIView):
    def get(self,respons,*args,**kwargs):
        greets = ""
        c_date = datetime.now()
        c_hour = c_date.hour
        if c_hour<12:
            greets = "Good Morning..."
        elif c_hour<18:
            greets = "Good Afternoon...."
        elif c_hour<24:
            greets = "Good Evening...."
        return Response({"msg":greets})

