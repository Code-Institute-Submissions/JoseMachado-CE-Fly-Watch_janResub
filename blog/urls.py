""" Fly Watch blog urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_flywatch, name='blog'),
    path('<int:post_id>/', views.blog_ind, name='blog_ind'),
    path('add/', views.add_blog, name='add_blog'),
    path('delete/<int:post_id>/', views.delete_blog, name='delete_blog'),
    path('edit/<int:post_id>/', views.edit_blog, name='edit_blog'),
]