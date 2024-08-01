from django.db import models
from django.contrib.auth.models import User
from products.models import Products

# Create your models here.
class Orderdetails(models.Model):
    user = models.ForeignKey(User , related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Products , related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'pending'), ('In-Transit', 'in-transit'), ('Delivered', 'delivered')])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_price_after_discount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('Cash', 'cash'), ('Card', 'card'), ('UPI', 'upi')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ['-created_at']
        verbose_name = 'Order' # this is used to change the name of the table in the admin site
        verbose_name_plural = 'Orders' # this is used to change the name of the table in the admin site

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
    

class OrderItems(models.Model):
    order = models.ForeignKey(Orderdetails , related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products , related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.order.user.username} - {self.product.name}'
