from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


user=get_user_model()

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    Active=models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    image=models.ImageField(blank=True,null=True)
    author=models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_snippet(self):
        return self.content[:5]
    
    def get_absolute_api_url(self):
        return reverse("blog:post", kwargs={"pk": self.pk})
    
    
class Category(models.Model):
    
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
    