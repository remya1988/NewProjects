from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AddView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        res = n1+n2
        return Response({"Added value = ":res})
class SubView(APIView):
    def post(self,request,*args,**kwargs):
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        res = n1 - n2
        return Response({"Subtracted value = ": res})
class MultView(APIView):
    def post(self,request,*args,**kwargs):
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        res = n1*n2
        return Response({"Multiplied value = ":res})
class CubView(APIView):
    def post(self,request,*args,**kwargs):
        n1 = request.data.get("num1")
        res = n1**3
        return Response({"Cube of number = ":res})
class FactView(APIView):
    def post(self,request,*args,**kwargs):
        n1 = request.data.get("num1")
        s = 1
        while(n1>0):
            s = s*n1
            n1 -= 1
        return Response({"Factorial of number = ":s})
class DivView(APIView):
    def post(self,request,*args,**kwargs):
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        res= n1/n2
        return Response({"Division = ": res})



