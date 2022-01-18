""" Fly Watch blog urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_flywatch, name='blog'),
    path('<int:post_id>/', views.blog_ind, name='blog_ind'),
]