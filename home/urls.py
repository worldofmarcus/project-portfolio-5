from django.urls import path
from blog.views import view_latest_blog_posts, blog_post_detail
from . import views

urlpatterns = [
    path('', view_latest_blog_posts, name='home'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]
