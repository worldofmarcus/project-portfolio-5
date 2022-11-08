from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import *


def list_all_posts(request):
    """ A view that lists all blog posts """

    posts = Post.objects.filter(status=1)

    # Pagination code
    p = Paginator(posts, 3)
    page = request.GET.get('page')
    blog_posts = p.get_page(page)
    # End of Pagination code

    context = {
        'blog_posts': blog_posts,
        }

    return render(request, 'home/index.html', context)


def blog_post_detail(request, slug):
    """ A view that lists a specific blog post """

    blog_post = get_object_or_404(Post, slug=slug)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_post_detail.html', context)
