from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    intro=models.TextField()
    body=models.TextField()
    posted_date=models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="Comment",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    body=models.TextField()
    posted_date=models.DateTimeField(auto_now_add=True)
    