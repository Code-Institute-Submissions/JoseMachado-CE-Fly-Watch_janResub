""" FlyWatch views """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PostBlog


def posts_flywatch(request):
    """ Page that returns with all posts """
    posts = PostBlog.objects.all().order_by('-post_date')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_ind(request, post_id):
    """ page will return the individual product """
    post = get_object_or_404(PostBlog, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_ind.html', context)
