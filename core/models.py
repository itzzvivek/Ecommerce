from sre_parse import CATEGORIES
from sys import flags
from turtle import title
from unicodedata import category
from django.db import models
from django.conf import settings

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
    category = models.CharField(choices=CATEGORIES_CHOICES, max_length=2 , default=())
    lable = models.CharField(choices=LABEL_CHOICES, max_length=1, default=())

    def _str_(self):
      return self.title


class OrderItem(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def _str_(self):
        return self.user.username