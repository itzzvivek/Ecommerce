from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Item
# Create your views here.

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)

def checkout(request):
    return render(request, "checkout.html")
    

class HomeView(ListView):
    model = Item
    template_name = "home.html"


def home(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "home.html", context)