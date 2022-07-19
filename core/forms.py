import email
from enum import Flag
from tkinter import Widget
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from setuptools import Require

PAYMENT_CHOICES = {
    ('s', 'Stripe'),
    ('P', 'Paypal')
}


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield( required= False, widget= CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))
    shipping_zip = forms.CharField()
    
   
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield( required= False, widget= CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))
    billing_zip = forms.CharField()

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices= PAYMENT_CHOICES)
     

class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form_control',
        'Placeholder': 'Promo code',
        'arial-label':'Recipients\'s username',
        'arial-discribedby': 'basic-adon2'
    }))

class RefundFrom(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea (attrs={
        'rows': 4
    }))
    email = forms.EmailField()