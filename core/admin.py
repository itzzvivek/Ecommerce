from re import I
from django.contrib import admin
from .models import Order, OrderItem, Payment, Item, Coupon

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Item)
admin.site.register(Payment)
admin.site.register(Coupon)
