from django.urls import path
from blog.views import list_all_posts, blog_post_detail

urlpatterns = [
    path('', list_all_posts, name='home'),
]
