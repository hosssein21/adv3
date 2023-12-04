from django.urls import path
from . import views

app_name='api-v1'
urlpatterns=[
    path('index/',views.index,name='index'),
    path('posts/',views.posts,name='posts'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
]