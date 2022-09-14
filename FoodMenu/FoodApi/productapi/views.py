from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from menulist.models import menu_items
from productapi.models import Product,Review,Carts,Orders
from productapi.serializer import ProductModelSerializer,UserSerializerr,ReviewSerializer,CartSerializer,OrderSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action

# Create your views here.
class ProductViewsetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Product.objects.all()
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
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serializer=ProductModelSerializer(qs)
        return Response(data=serializer.data)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Product.objects.get(id=id)
        serializer=ProductModelSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Product.objects.get(id=id)
        serializer = ProductModelSerializer(instance)
        instance.delete()
        return Response({"msg": "deleted"})
class ProductModelViewsetView(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset=Product.objects.all()
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    @action(methods=["post"],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Product.objects.get(id=id)
        user=request.user
        serializer=CartSerializer(data=request.data,context={"user":user,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["post"], detail=True)
    def order_palced(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Product.objects.get(id=id)
        user=request.user
        serializer=OrderSerializer(data=request.data,context={"user":user,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    @action(methods=["get"],detail=True)
    def get_reviews(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Product.objects.get(id=id)
        review=product.review_set.all()
        serializer=ReviewSerializer(review,many=True)
        return Response(data=serializer.data)
    @action(methods=["post"],detail=True)
    def post_review(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        product = Product.objects.get(id=id)
        author=request.user
        review=request.data.get("review")
        rating=request.data.get("rating")
        qs=Review.objects.create(author=author,product=product,review=review,rating=rating)
        serializer=ReviewSerializer(qs)
        return Response(data=serializer.data)


class UserModelViewsetView(ModelViewSet):
    serializer_class = UserSerializerr
    queryset = User.objects.all()

class CartView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Carts.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs=Carts.objects.filter(user=request.user)
        serializer=CartSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        return Response(data={"msg":"no access"})