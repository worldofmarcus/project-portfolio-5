from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def list_all_products(request):
    """ A view that lists all products """

    # Pagination code
    p = Paginator(Product.objects.all(), 6)
    page = request.GET.get('page')
    product_list = p.get_page(page)
    # End of Pagination code


    total_products = Product.objects.all().count()
    context = {
        'total_products': total_products,
        'product_list': product_list,
        }

    return render(request, 'products/products.html', context)