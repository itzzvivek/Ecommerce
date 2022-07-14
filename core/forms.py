from tkinter import Widget
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = {
    ('s', 'Stripe'),
    ('P', 'Paypal')
}


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={'PlaceHolder': '1234 Main St'}))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={'PlaceHolder': 'Apartment or Suite'}))
    country = CountryField(blank_label='(select country)').formfield(widget= CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form_control',
        'Placeholder': 'Promo code',
        'arial-label':'Recipients\'s username',
        'arial-discribedby': 'basic-adon2'
    }))

class RefundFrom(forms.From):
    ref_code = forms.CharFeild()
    message = forms.Textarea()