from django.contrib import admin
from .models import Product, Tag, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Category)