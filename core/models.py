import imp
from pydoc import describe
from sre_parse import CATEGORIES
from statistics import quantiles
from sys import flags
from turtle import title
from unicodedata import category
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

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def _str_(self):
        return self.user.username