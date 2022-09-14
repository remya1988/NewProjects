from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from menulist.models import menu_items
from productapi.models import Product
from productapi.serializer import ProductModelSerializer
from rest_framework.viewsets import ViewSet

# Create your views here.
class MenuItemView(APIView):
    def get(self,request,*args,**kwargs):
        all_item =menu_items
        if "category" in request.query_params:
            cat = request.query_params.get("category")
            all_item = [item for item in all_item if item["category"] == cat]
            #return Response(data=item)
        if "limit" in request.query_params:
            limit = int(request.query_params.get("limit"))
            all_item =all_item[:limit]
        #return Response(data=all_item)
        if "price" in request.query_params:
            pric = int(request.query_params.get("price"))
            all_item = [item for item in all_item if  item["price"]>pric]
           # return Response(data=item)
        return Response(data=all_item)
            #return Response(data=menu_items)
    def post(self,request,*args,**kwargs):
        data = request.data
        menu_items.append(data)
        return Response(data=data)
class MenuDetailsView(APIView):
    def get(self,request,*args,**kwargs):
         mid=kwargs.get("mid")
         item = [item for item in menu_items if item["code"]==mid].pop()
         return Response(data=item)
    def delete(self,request,*args,**kwargs):
        id = kwargs.get("mid")
        item = [item for item in menu_items if item["code"]==id].pop()
        menu_items.remove(item)
        return Response(data=menu_items)

