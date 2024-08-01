from rest_framework import serializers
from .models import Orderdetails, OrderItems

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Orderdetails
        fields = ['user', 'product', 'quantity', 'ordered_date', 'status', 'total_price', 'total_discount', 'total_price_after_discount', 'payment_method', 'created_at', 'updated_at', 'items']

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = ['id', 'user', 'product', 'quantity', 'ordered_date', 'status', 'total_price', 'total_discount', 'total_price_after_discount', 'payment_method', 'created_at', 'updated_at']
