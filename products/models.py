from django.db import models

class Product(models.Model):
    """ Product model """

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = models.ManyToManyField(Tag)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    product_size = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name