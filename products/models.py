from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


STATUS = ((0, 'Draft'), (1, 'Published'))


class Tag(models.Model):

    """ Tag model """
    name = models.CharField(max_length=200, null=True)
    view_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    """ Category model """
    class Meta:
        verbose_name_plural = 'Categories'  # Fix plural bug in admin area

    name = models.CharField(max_length=254)
    view_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_view_name(self):
        return self.view_name


class Product(models.Model):

    """ Product model that will provide all the products
    that are for sale in the store. """

    class Meta:
        """
        This meta class orders the model by date.
        """

        ordering = ['-date']

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.0, message=None)])
    tags = models.ManyToManyField(Tag)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    sku = models.CharField(max_length=254, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    product_size = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    users_wishlist = models.ManyToManyField(User)

    def __str__(self):
        return self.name
