from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from ...models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

@api_view()
def index(request):
    return Response({"detail":'index data'})


@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
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
    
class PostList(APIView):
    
    serializer_class = PostSerializer
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class PostDetail(APIView):
    
    def get(self,request,pk):
        try:
            post=Post.objects.filter(Active=1,pk=pk)
            serializer=PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"detail":'data not found'},status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        post=Post.objects.filter(Active=1,pk=pk)
        serializer=PostSerializer(post,data=request.dat)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        post=Post.objects.filter(Active=1,pk=pk)
        post.delete()
        return Response({"detail":"data deleted"},status=status.HTTP_204_NO_CONTENT)
    
class PostListGeneric(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset =Post.objects.all()
    
class PostDetailGeneric(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes =[IsAuthenticated]
    queryset =Post.objects.filter(Active=1)
    

    
    