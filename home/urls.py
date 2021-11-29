from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
]
