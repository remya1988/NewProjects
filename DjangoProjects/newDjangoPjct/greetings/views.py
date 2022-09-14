from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class GoodmorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"goodmng"})

class GoodAfternoonView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good After Noon"})

