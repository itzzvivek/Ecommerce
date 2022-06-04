from sys import flags
from turtle import title
from django.db import models
from django.conf import settings

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

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