from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog

@login_required
def blog_home(request):
    blogs = Blog.objects
    context = {
        'blogs' : blogs
    }
    return render(request, 'blog/home.html', context)

@login_required
def blog_about(request):
    return render(request, 'blog/about.html')

@login_required
def blog_detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog' : blog_detail
    }
    return render(request, 'blog/detail.html', context)
    