from django.shortcuts import render
from django.core.paginator import Paginator

from .models import *


def list_all_posts(request):
    """ A view that lists all blog posts """

    posts = Post.objects.all()

    # Pagination code
    p = Paginator(posts, 3)
    page = request.GET.get('page')
    blog_posts = p.get_page(page)
    # End of Pagination code

    context = {
        'blog_posts': blog_posts,
        }

    return render(request, 'home/index.html', context)
