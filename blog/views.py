# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.db import models
from .forms import PostForm,LinkForm
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
import urllib
from . import inst
from django.core.files import File
from io import BytesIO
from django.contrib.auth.decorators import login_required



def post_list(request):
	posts = Post.objects.filter(date__lte=timezone.now()).order_by('date')
	return render(request, 'blog/post_list.html', {'posts': posts,'MEDIA_URL': settings.MEDIA_URL})

@login_required
def add_post(request):
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form}) 

@login_required
def add_link(request):
    form = LinkForm(request.POST)
    
    if form.is_valid():
        userLink=request.POST['link']
        photoDescrDate=inst.getMediaByLink(userLink)
        name = photoDescrDate[0][-30:]
        #ph=urllib.request.urlretrieve(photoDescrDate[0], '.'+settings.MEDIA_URL+name)
        response =urllib.request.urlopen(photoDescrDate[0])
        io = BytesIO(response.read()) 
        print(photoDescrDate[0])
        post=Post( title='From Instagram',text=photoDescrDate[1],date=photoDescrDate[2],author=request.user )
        #content = urllib.request.urlretrieve(photoDescrDate[0])
        post.photo.save(name, File(io), save=True)
    

        return redirect('post_list' )
    else:
        form = LinkForm()     
    return render(request, 'blog/add_link.html', {'form': form})     

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'MEDIA_URL': settings.MEDIA_URL})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/add_post.html', {'form': form,'MEDIA_URL': settings.MEDIA_URL, 'user':request.user})    

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')    