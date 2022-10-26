from django.shortcuts import render
from .models import Product

# Create your views here.

def list_all_products(request):
    """ A view that lists all products """

    products = Product.objects.all()

    context = {
        'products': products,
        }

    return render(request, 'products/products.html', context)