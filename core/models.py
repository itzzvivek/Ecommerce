from pyexpat import model
from tkinter import CASCADE
from turtle import Turtle
from typing import Tuple
from django_countries.fields import CountryField
from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

CATEGORIES_CHOICES = (
    ('S', 'Shirt'),
    ('SM', 'Sport wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True , null=True)
    category = models.CharField(choices=CATEGORIES_CHOICES, max_length=2 , default=())
    lable = models.CharField(choices=LABEL_CHOICES, max_length=1, default=())
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def _str_(self):
      return self.title

    def get_absolute_url(self):
         return reverse("core:product", kwargs ={
        'slug': self.slug
    })

    def get_add_to_cart_url(self):
        return reverse ("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse ("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def _str_(self):
        return f"{self.quantity} of {self.item.title} "

    def get_total_item_price(self):
        return self.quantity * self.item.discount_price
    
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_amount_saved(self):
        return self.get_totle_price_item_price - self.total_discount_item_price()
    
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_disount_item_price()
        return self.get_total_item_price()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True )
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True )

    def _str_(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.item.all():
            total += order_item.get_final_price()
        return total

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple= False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username