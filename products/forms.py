from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    This class creates the product form.
    """
    class Meta:
        """
        This meta class adds the fields to the form
        based on the product model. It also adds a number
        of widgets to customize and add functionality
        to the form.
        """

        model = Product
        fields = ('category', 'name', 'price', 'product_size', 'description',
                  'image', 'tags', 'status',)
        widgets = {
                    'category': forms.Select(
                        attrs={'class': 'form-select'}),
                    'status': forms.Select(attrs={'class': 'form-select'}),
                    }

    def __init__(self, *args, **kwargs):
        """
        This method returns a friendly category
        view name.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_view_name = [(c.id, c.get_view_name()) for c in categories]

        self.fields['category'].choices = category_view_name
