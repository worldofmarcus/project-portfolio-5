"""Import relevant modules for the application"""

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    This class handles the UserProfileForm
    (based on the UserProfile model)
    """

    class Meta:
        model = UserProfile
        exclude = ('user',)
        widgets = {
                    'default_country': forms.Select(
                        attrs={'class': 'form-select'}),
                    }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
            'default_country': 'Country',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
