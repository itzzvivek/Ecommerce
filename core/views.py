import imp
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import redirect 
from django.utils import timezone
from .models import Item, OrderItem,Order
# Create your views here.

def product(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)

def checkout(request):
    return render(request, "checkout.html")
    

class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False
        )
    order_qs = Order.objects.filter(user=request.user, ordered= False) #qs = QuerySet
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item_slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated ") #leave 49:34

        else:
            messages.info(request, "This was added to your cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.item.add(order_item)
    return redirect("core:product", slug=slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered= False
    ) #qs = QuerySet
    
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item_slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered = False
                )[0]
            order.item.remove(order_item)
        else:
            #add a message saying the user dosn't have an order
            return redirect("core:product", slug=slug)

    else:
        #add a message saying the user dosn't have an order
        return redirect("core:product", slug=slug)
    return redirect("core:product", slug=slug)
      


    