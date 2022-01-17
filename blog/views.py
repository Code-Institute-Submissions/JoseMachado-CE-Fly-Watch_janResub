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