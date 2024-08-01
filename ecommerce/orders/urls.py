from django.urls import path
from .views import checkout, OrdersList, add_to_cart

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('orders/', OrdersList.as_view(), name='orders-list'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
]