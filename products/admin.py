"""Import relevant modules for the application"""

from django.contrib import admin
from .models import Product, Tag, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    This class adds fields from the Product model to the admin
    area and also add list functionality (i.e ordering and possibility
    to execute actions).
    """

    list_display = (

        'sku',
        'date',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)
    actions = ['publish', 'unpublish']

    def publish(self, request, queryset):
        """
        This help method updates the status field to 1
        """

        queryset.update(status=1)

    def unpublish(self, request, queryset):
        """
        This help method updates the status field to 0
        """

        queryset.update(status=0)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    This class adds fields from the Tag model to the admin
    area.
    """

    list_display = (
        'view_name',
        'name',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class adds fields from the Category model to the admin
    area.
    """

    list_display = (
        'view_name',
        'name',
    )
