from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()

    newest_posts = Post.objects.all().order_by('-date_posted')[0:1]

    context = {
        'posts' : posts,
        'newest_posts' : newest_posts
    }
    return render(request,'home.html',context)

def post(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post' : post,
    }
    return render(request,'post.html',context)

def about_me(request):
    
    return render(request,'about_me.html')