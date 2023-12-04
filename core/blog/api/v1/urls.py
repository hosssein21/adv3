from django.urls import path
from . import views

app_name='api-v1'
urlpatterns=[
    path('index/',views.index,name='index'),
    path('posts/',views.PostListGeneric.as_view(),name='posts'),
    path('post/<int:pk>/',views.PostDetailGeneric.as_view(),name='post_detail'),
]