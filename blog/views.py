from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from .forms import CreateBlogPostForm

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

@login_required
def add_blog_post(request):
    """ This view adds a blog post to the site """

    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CreateBlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.title)
            post = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('blog_post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = CreateBlogPostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)