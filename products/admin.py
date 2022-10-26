from django.contrib import admin
from .models import Product, Tag, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'view_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)