from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ecompdt.models import products

# Create your views here.
class ProdView(APIView):
    def get(self,request,*args,**kwargs):
        if "price_lte" in request.query_params:
            price = request.query_params.get("price_lte")
            #print(price)
            prod =[prod for prod in products if prod["price"]<=70]
            return Response(data=prod)
        elif "limit" in request.query_params:
            limit = int(request.query_params.get("limit"))
            prod = [prod for prod in products]
            p=[]
            for i in range(limit):
                p.append(prod[i])
            return Response(data=p)

        return Response(data=products)
    def post(self,request,*args,**kwargs):
        data = request.data
        products.append(data)
        return Response(data=data)
class ProdDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        pid = kwargs.get("pid")
        prod = [prod for prod in products if prod["id"]==pid].pop()
        return Response(data=prod)
    def put(self,request,*args,**kwargs):
        pid = kwargs.get("pid")
        prod = [prod for prod in products if prod["id"]==pid].pop()
        prod.update(request.data)
        return Response(data=prod)
    def delete(self, request,*args,**kwargs):
        pid = kwargs.get("pid")
        prod = [prod for prod in products if prod["id"]==pid].pop()
        products.remove(prod)
        return Response(data=prod)

