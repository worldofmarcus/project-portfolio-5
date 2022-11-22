"""Import relevant modules for the application"""

from django.urls import path
from . import views

urlpatterns = [
    path('edit/<slug:slug>/', views.edit_blog_post, name='edit_blog_post'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
    path('delete/<slug:slug>/', views.delete_blog_post,
         name='delete_blog_post'),
    path('', views.view_all_blog_posts,
         name='view_all_blog_posts'),
]
