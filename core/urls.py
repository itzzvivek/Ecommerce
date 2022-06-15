from django.urls import path
from .views import item_list
from.import views

app_name = 'core'

urlpatterns = [
    
    path("",views.item_list,name='item_list')
]