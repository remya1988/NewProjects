from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from menus.models import Dishes
from menus.serializers import ProductSerializers,ProductModelSerializer
from rest_framework import status
from rest_framework.viewsets import ViewSet

# Create your views here.
class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer = ProductSerializers(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serializer=ProductSerializers(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid():
            instance.name=serializer.validated_data.get("name")
            instance.category=serializer.validated_data.get("category")
            instance.price=serializer.validated_data.get("price")
            instance.rating=serializer.validated_data.get("rating")
            instance.save()
            #instance.update(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        id =kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializer=ProductSerializers(instance)
        instance.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

class ProductModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category=request.query_params.get("category"))
        if "price__gt" in request.query_params:
            qs=qs.filter(price__gte=request.query_params.get("price__gt"))
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    def post(self,request,*args,**kwargs):
        serializer=ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailsModelView(APIView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs =Dishes.objects.get(id=id)
        serializer=ProductModelSerializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        object=Dishes.objects.get(id=id)
        serializer=ProductModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ProductViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer=ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs=Dishes.objects.get(id=id)
        serializer=ProductModelSerializer(qs)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object=Dishes.objects.get(id=id)
        serializer=ProductModelSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        instance=Dishes.objects.get(id=id)
        serializer=ProductModelSerializer(instance)
        instance.delete()
        return Response({"msg":"deleted"})