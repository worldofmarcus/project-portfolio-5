from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from .forms import CreateBlogPostForm

from .models import *


def view_latest_blog_posts(request):
    """ A view that lists all blog posts """

    posts = Post.objects.filter(status=1)
    category = None

    # Pagination code
    p = Paginator(posts, 3)
    page = request.GET.get('page')
    blog_posts = p.get_page(page)
    # End of Pagination code

    context = {
        'blog_posts': blog_posts,
        'category': category,
        }

    return render(request, 'home/index.html', context)


def view_all_blog_posts(request):
    """ A view that lists all blog posts """

    posts = Post.objects.filter(status=1)
    category = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            posts = posts.filter(category=category)

    # Pagination code
    p = Paginator(posts, 9)
    page = request.GET.get('page')
    blog_posts = p.get_page(page)
    # End of Pagination code

    context = {
        'blog_posts': blog_posts,
        'category': category,
        }

    return render(request, 'blog/view_all_blog_posts.html', context)


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

    posts = Post.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               'You did not enter any search criteria!')
                return redirect(reverse('add_product'))
            queries = Q(title__icontains=query) | Q(body__icontains=query)
            posts = posts.filter(queries)

    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CreateBlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.title)
            post = form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(
                reverse('blog_post_detail', args=[form.instance.slug]))
        else:
            messages.error(request,
                           'Failed to add blog post. '
                           'Please ensure the form is valid.')
    else:
        form = CreateBlogPostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
        'posts': posts,
    }
    return render(request, template, context)


@login_required
def edit_blog_post(request, slug):
    """ This view makes it possible to edit a blog post
    on the site """

    posts = Post.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               'You did not enter any search criteria!')
                return redirect(reverse('add_product'))
            queries = Q(title__icontains=query) | Q(body__icontains=query)
            posts = posts.filter(queries)

    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CreateBlogPostForm(
            request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.title)
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_post_detail', args=[blog_post.slug]))
        else:
            messages.error(request, 'Failed to update blog post. '
                           'Please ensure the form is valid.')
    else:
        form = CreateBlogPostForm(instance=blog_post)
        messages.info(request, f'You are editing {blog_post.title}.')

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'blog_post': blog_post,
        'posts': posts,
    }
    return render(request, template, context)


@login_required
def delete_blog_post(request, slug):
    """ This view will delete a blog post from the site """

    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(Post, slug=slug)
    blog_post.delete()
    messages.success(request, 'Successfully deleted the blog post!')
    return redirect(reverse('add_blog_post'))
