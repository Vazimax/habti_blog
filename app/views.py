from django.shortcuts import render
from .models import Post


def home(request):

    return render(request,'home.html')

def post(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post' : post,
    }
    return render(request,'post.html',context)

def about_me(request):
    
    return render(request,'about_me.html')