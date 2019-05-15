from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

# Create your views here.
def home(request):
    Blogs = Blog.objects.all()
    return render(request, 'home.html', {'Blogs':Blogs})

def detail(request,post_id):
    blog = get_object_or_404(Blog, pk=post_id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = Blog()
    new_post.title=request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.body=request.POST['body']
    new_post.save()
    return redirect('home')

def edit(request, post_id):
    edit_post = Blog.objects.get(id=post_id)
    return render(request, 'edit.html', {'blog':edit_post})

def update(request, post_id):
    update_post = Blog.objects.get(id=post_id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('home')

def delete(request, post_id):
    delete_post=Blog.objects.get(id=post_id)
    delete_post.delete()
    return redirect('home')

    