from django.db import models
from products.models import Products
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='uploads/avatars/', null=True, blank=True)
    Product = models.ManyToManyField(Products, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username