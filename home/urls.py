from django.urls import path
from blog.views import list_all_posts, blog_post_detail
from . import views

urlpatterns = [
    path('', list_all_posts, name='home'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]
