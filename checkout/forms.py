from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    """Class which allows payments to be made"""
    MONTH_CHOICES = [(i, i) for i in range(1,12)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]

    #Required set to false to prevent data from being sent in the browser = more secure
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput) #Hidden from the user

class OrderForm(forms.ModelForm):
    """Inherit from .ModelForm as we are using a model from another app"""
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')
