from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models.functions import Lower

from .models import *
from .forms import ProductForm


def list_all_products(request):
    """ A view that lists all products """

    products = Product.objects.all()
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
                # if sortkey == 'category':
                #     sortkey = 'category__name'

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
                messages.error(request, 'You did not enter any search criteria!')
                return redirect(reverse('list_all_products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # # Pagination code
    # p = Paginator(products, 6)
    # page = request.GET.get('page')
    # product_list = p.get_page(page)
    # # End of Pagination code

    product_list = products

    current_sorting = f'{sort}_{direction}'

    context = {
        'total_products': total_products,
        'product_list': product_list,
        'search_term': query,
        'current_categories': categories,
        'category': category,
        'current_sorting': current_sorting,
        'sort': sort,
        'direction': direction,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view that lists a specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ This view adds a product to the site """

    form = ProductForm
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)