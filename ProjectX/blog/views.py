from sqlite3 import Timestamp
from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)

def createPost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        user = request.user
        image = request.FILES.get('images')
        content = request.POST.get('content')
        post = Post(title=title, slug=slug, author=user, image=image, content=content)
        post.save()
        messages.success(request, "post submitted")
    return render(request, 'blog/UserPost.html')