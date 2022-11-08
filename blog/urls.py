from django.urls import path
from . import views

urlpatterns = [
    path('blog/add/', views.add_blog_post, name='add_blog_post'),
]