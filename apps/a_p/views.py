from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.core import serializers

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'a_p/index.html', context)

def create(request):
    post = Post(post=request.POST['new_post'])
    post.save()
    print post
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'a_p/all.html', context)
    
    
    