from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    This meta class creates the orderform and
    also add extra styling through widgets
    """

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)
        widgets = {
                    'country': forms.Select(
                        attrs={'class': 'form-select'}),
                    }

    def __init__(self, *args, **kwargs):
        """
        This view adds classes and placeholders to the fields in the
        order model. It also removes auto-generated labels and sets
        the autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:

            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
