from django.urls import path
from django.views import View
from .views import (ItemDetailView , checkout ,HomeView)
from.import views

app_name = 'core'

urlpatterns = [
    
    path("", HomeView.as_view(), name='item_list'),
    path('checkout/', checkout, name= 'checkout'),
    path('product/<slug>/',ItemDetailView.as_view(), name = 'product')
]   