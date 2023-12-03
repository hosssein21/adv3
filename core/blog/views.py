from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView,ListView,DeleteView,CreateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Post

class IndexView(TemplateView):
    
    template_name='blog/index.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["name"]="hosssein"
        return context
    
class Redirect(RedirectView):
    url = 'http://google.com/'
    
class PostList(ListView):
    template_name="blog/posts.html"
    model=Post
    context_object_name="posts"
    
class PostDetail(PermissionRequiredMixin,DeleteView):
    permission_required = 'blog.view_post'
    template_name="blog/post.html"
    queryset=Post.objects.filter(Active=1)
    
class PostCreate(LoginRequiredMixin,CreateView):
    template_name="blog/create.html"
    model=Post
    fields=["title","content","author","category"]
    success_url="/blog/posts/"
    
class PostUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'blog.update_post'
    template_name="blog/create.html"
    model=Post
    fields=["title","content"]
    success_url="/blog/posts/"
    
class PostDelete(DeleteView):
    
    template_name="blog/delete.html"
    model=Post
    success_url="/blog/posts/"
    

