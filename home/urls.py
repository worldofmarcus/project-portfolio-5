from django.urls import path
from blog.views import list_all_posts

urlpatterns = [
    path('', list_all_posts, name='home'),
]
