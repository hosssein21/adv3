from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name='api-v1'

router = DefaultRouter()
router.register('post', views.PostViewSet,basename='post')
router.register('category', views.CategoryViewSet,basename='category')
urlpatterns = router.urls


# urlpatterns=[
#     path('index/',views.index,name='index'),
#     path('posts/',views.PostListGeneric.as_view(),name='posts'),
#     path('post/<int:pk>/',views.PostDetailGeneric.as_view(),name='post_detail'),
# ]