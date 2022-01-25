""" FlyWatch views """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PostBlog
from .forms import BlogForm


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


@login_required
def add_blog(request):
    """ function to add post to blog """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only admin can do this.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully post added!')
            return redirect(reverse('blog_ind', args=[post.id]))
        else:
            messages.error(
                request,
                'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_blog.html', context)


@login_required
def delete_blog(request, post_id):
    """ Delete a blog post on blog page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, \
            admins authorised to do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(PostBlog, pk=post_id)
    post.delete()
    messages.success(request, f'Blog post: {post.title} deleted!')
    return redirect(reverse('blog'))


@login_required
def edit_blog(request, post_id):
    """ Function to edit blog posts """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin can do such.')
        return redirect(reverse('home'))
    post = get_object_or_404(PostBlog, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post updated!!')
            return redirect(reverse('blog_ind', args=[post.id]))
        else:
            messages.error(
                request, 'It was not this time. Please, Try it again!')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)
