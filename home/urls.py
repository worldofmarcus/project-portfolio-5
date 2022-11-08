from django.urls import path
from blog.views import list_all_posts, blog_post_detail

urlpatterns = [
    path('', list_all_posts, name='home'),
    path('blog/<slug:slug>/', blog_post_detail, name='blog_post_detail'),
]
