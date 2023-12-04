from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from ...models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

@api_view()
def index(request):
    return Response({"detail":'index data'})


@api_view(["GET","PUT","DELETE"])
@permission_classes[IsAuthenticated]
def post_detail(request,pk):
    if request.method=="GET":
        try:
            post=Post.objects.filter(Active=1)
            serializer=PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"detail":'data not found'},status=status.HTTP_404_NOT_FOUND)
        
    elif request.method=="PUT":
        post=Post.objects.filter(Active=1)
        serializer=PostSerializer(post,data=request.dat)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method=="DELETE":
        post=Post.objects.filter(Active=1)
        post.delete()
        return Response({"detail":"data deleted"},status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET", "POST"])  
def posts(request):
    if request.method == "GET":
        post=Post.objects.all()
        serializer=PostSerializer(post,many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)