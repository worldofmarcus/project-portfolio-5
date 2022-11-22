"""Import relevant modules for the application"""

from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class adds fields from the Category model to the admin
    area and also add list functionality.
    """

    list_display = ('name', )
    list_filter = ('name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    This class adds fields from the Post model to the admin
    area and also add functionality like approve review and
    publish in the action dropdown list.
    """

    list_display = ('title', 'slug', 'category', 'status', 'date_created_on',
                    'author',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created_on')
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
