from django.db import models

# Create your models here.
from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
