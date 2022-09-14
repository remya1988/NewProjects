from rest_framework import serializers
from django.contrib.auth.models import User
from socialapi.models import UserProfile,Posts,Comments


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email"
        ]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    following=serializers.CharField(read_only=True)
    class Meta:
        model=UserProfile
        fields="__all__"

    def create(self,validated_data):
        user=self.context.get("user")
        return UserProfile.objects.create(user=user,**validated_data)



class CommentSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    post=serializers.CharField(read_only=True)
    class Meta:
        model=Comments
        exclude=("date",)
    def create(self,validated_data):
        post=self.context.get("post")
        user=self.context.get("user")
        return Comments.objects.create(user=user,post=post,**validated_data)

class PostSerializer(serializers.ModelSerializer):
    author=serializers.CharField(read_only=True)
    fetch_comments = CommentSerializer(read_only=True,many=True)
    liked_by=UserSerializer(read_only=True,many=True)
    count_like=serializers.CharField(read_only=True)

    class Meta:
        model=Posts
        fields="__all__"

class CommentListSerializer(serializers.ModelSerializer):
    author=serializers.CharField(read_only=True)
    title=serializers.CharField(read_only=True)
    comment=serializers.CharField(read_only=True)
    datetime=serializers.DateField(read_only=True)
    class Meta:
        model=Comments
        fields="__all__"


