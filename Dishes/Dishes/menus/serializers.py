from rest_framework import serializers
from menus.models import Dishes
class ProductSerializers(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name=serializers.CharField(max_length=120)
    category=serializers.CharField(max_length=120)
    price=serializers.IntegerField()
    rating=serializers.FloatField()
    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("Invalid value")
        return data
class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields="__all__"