from rest_framework import serializers
from productapi.models import Product,Carts,Review,Orders
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.DateField(read_only=True)
    status=serializers.CharField(read_only=True)
    expected_delivery_date=serializers.DateField(read_only=True)
    class Meta:
        model=Orders
        fields=[
            "user",
            "product",
            "date",
            "status",
            "expected_delivery_date"
        ]
    def create(self,validated_date):
        user=self.context.get("user")
        product=self.context.get("product")
        return Orders.objects.create(**validated_date,user=user,product=product)

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.DateField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=[
            "user",
            "product",
            "qty",
            "date",
            "status"
        ]
    def create(self,validated_date):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(user=user,product=product)

class ProductModelSerializer(serializers.ModelSerializer):
    avg_rating =serializers.CharField(read_only=True)
    review_count=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Product
        fields=[
            "id",
            "p_name",
            "category",
            "price",
            "avg_rating",
            "review_count"

        ]


class UserSerializerr(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class ReviewSerializer(serializers.ModelSerializer):
    author=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields="__all__"