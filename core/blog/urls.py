from django.urls import path,include
from . import views

app_name='blog'
urlpatterns = [
    path('index/',views.IndexView.as_view(),name='index'),
    path('redirect/',views.Redirect.as_view(),name='redirect'),
    path('posts/',views.PostList.as_view(),name='posts'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post'),
    path('post/create/',views.PostCreate.as_view(),name='create'),
    path('post/update/<int:pk>/',views.PostUpdate.as_view(),name='update'),
    path('post/delete/<int:pk>/',views.PostDelete.as_view(),name='delete'),
    path('api/v1/',include('blog.api.v1.urls')),
]
