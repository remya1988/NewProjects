from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    prof_pic=models.ImageField(upload_to="profpic",null=True)
    phone=models.CharField(max_length=12)
    dob=models.DateField(null=True,auto_created=True)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=12)
    bio=models.CharField(max_length=200)
    following=models.ManyToManyField(User,null=True,related_name="following")


class Posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    image=models.ImageField(upload_to="postimg",null=True)
    date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)

    def __str__(self):
         return self.title

    def fetch_comments(self):
         return self.comments_set.all()

    def count_like(self):
        return self.liked_by.all().count()

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)