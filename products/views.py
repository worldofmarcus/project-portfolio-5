"""Import relevant modules for the application"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models.functions import Lower

from .models import *
from .forms import ProductForm


def list_all_products(request):
    """ This view lists all products depending on what
    is included in the GET request (i.e. category and sort).
    It also handles the pagination on the page.
    """

    products = Product.objects.filter(status=1)
    query = None
    categories = None
    category = None
    sort = None
    direction = None
    tag = None

    total_products = Product.objects.all().count()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'tag' in request.GET:
            tag = request.GET['tag']
            products = products.filter(tags__name=tag)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            category = request.GET['category']
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 'You did not enter any search criteria!')
                return redirect(reverse('list_all_products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Pagination code
    p = Paginator(products, 9)
    page = request.GET.get('page')
    products = p.get_page(page)
    # End of Pagination code

    current_sorting = f'{sort}_{direction}'

    context = {
        'total_products': total_products,
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'category': category,
        'current_sorting': current_sorting,
        'sort': sort,
        'direction': direction,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """This view lists a specific product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """This view adds a product to the site"""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 'You did not enter any search criteria!')
                return redirect(reverse('add_product'))
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product.'
                'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'products': products,
        'search_term': query,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    This view makes it possible to edit a product
    on the site
    """

    products = Product.objects.all()

    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product.'
                'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}.')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'products': products,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """This view will delete a product from the site"""

    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted product!')
    return redirect(reverse('add_product'))
