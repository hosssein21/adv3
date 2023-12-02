from django.db import models
from django.contrib.auth import get_user_model

user=get_user_model()

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    Active=models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    image=models.ImageField(blank=True,null=True)
    author=models.ForeignKey(user,on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
    