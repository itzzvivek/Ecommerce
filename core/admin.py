from re import I
from django.contrib import admin
from .models import Order, OrderItem, Payment, Item, Coupon

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'ordered',
        'being_delivered', 
        'recived', 
        'refund_requested', 
        'refund_granted',
        'billings_address',
        'payments',
        'coupon'
        ]
    list_display_link = [
        'user',
        'billings_address',
        'payments',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_request',
                   'refund_granted'
                   ]
        
    search_fields = [
        'user__username',
        'ref_code']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Item)
admin.site.register(Payment)
admin.site.register(Coupon)
