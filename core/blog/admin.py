from django.contrib import admin
from .models import Post,Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display=["title","author","Active"]
    search_fields =("title","content")
    list_filter=("Active",)
    
admin.site.register(Category)
    
    
