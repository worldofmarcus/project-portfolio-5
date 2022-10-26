from django.shortcuts import render
from .models import *

# Create your views here.

def list_all_products(request):
    """ A view that lists all products """

    products = Product.objects.all()
    total_products = products.count()

    context = {
        'products': products,
        'total_products': total_products,
        }

    return render(request, 'products/products.html', context)