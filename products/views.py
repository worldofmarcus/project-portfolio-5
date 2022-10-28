from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def list_all_products(request):
    """ A view that lists all products """

    products = Product.objects.all()
    query = None
    categories = None
    category = None

    total_products = Product.objects.all().count()

    if request.GET:
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

    # Pagination code
    p = Paginator(products, 6)
    page = request.GET.get('page')
    product_list = p.get_page(page)
    # End of Pagination code


    context = {
        'total_products': total_products,
        'product_list': product_list,
        'search_term': query,
        'current_categories': categories,
        'category': category

        }

    return render(request, 'products/products.html', context)