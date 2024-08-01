from django.contrib import admin
from .models import Orderdetails, OrderItems

# Register your models here.
admin.site.register(Orderdetails)
admin.site.register(OrderItems)
