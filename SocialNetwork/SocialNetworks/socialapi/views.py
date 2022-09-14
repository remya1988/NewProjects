from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from socialapi.serializer import UserSerializer,UserProfileSerializer,PostSerializer,CommentSerializer,CommentListSerializer
from django.contrib.auth.models import User
from socialapi.models import UserProfile,Posts,Comments
from rest_framework import permissions,authentication
from rest_framework.decorators import action

# Create your views here.

class UserRegistrationView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):
        user=request.user
        serializer=UserProfileSerializer(data=request.data,context={"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    # http://127.0.0.1:8000/api/v1/user/profile/{pk}/add_followers
    @action(methods=["post"],detail=True)
    def add_followers(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        follow_user=User.objects.get(id=id)
        profile=UserProfile.objects.get(user=request.user)
        profile.following.add(follow_user)
        return Response({"msg":"ok"})

    #api/v1/user/profile/my_following/
    @action(methods=["get"],detail=False)
    def my_following(self,request,*args,**kwargs):
        user=request.user
        user_profile=UserProfile.objects.get(user=user)
        following=user_profile.following.all()
        #seriaizer=UserSerializer(following,many=True)
        # get_following=request.user.following.all()
        # print(get_following)
        serializer=UserSerializer(following,many=True)

        return Response(data=serializer.data)



class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    # http://127.0.0.1:8000/api/v1/post/1/add_comment/
    @action(methods=["post"],detail=True)
    def add_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        user=request.user
        serializer=CommentSerializer(data=request.data,context={"user":user,"post":post})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    # http://127.0.0.1:8000/api/v1/post/1/list_comment/
    @action(methods=["get"],detail=True)
    def list_comments(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        comments=post.comments_set.all()
        serializer=CommentListSerializer(comments,many=True)
        return Response(data=serializer.data)

    #http://127.0.0.1:8000/api/v1/post/1/add_like/
    @action(methods=["post"],detail=True)
    def add_like(selfself,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        post.liked_by.add(request.user)
        return Response({"Message":"ok"})

