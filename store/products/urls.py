from django.urls import path
from .views import products, basket_add
app_name = 'products'       

urlpatterns = [
    path('products/', products, name='index'),
    path('basket/', basket_add, name='basket')
]