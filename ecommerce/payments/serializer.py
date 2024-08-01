from rest_framework import serializers
from .models import Payment
from decimal import Decimal

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'order_id', 'amount', 'currency', 'payment_method', 'payment_status')

    def create(self, validated_data):
        validated_data['amount'] = float(validated_data['amount'])  # Convert Decimal to float
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_id = validated_data.get('order_id', instance.order_id)
        instance.amount = float(validated_data.get('amount', instance.amount))  # Convert Decimal to float
        instance.currency = validated_data.get('currency', instance.currency)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.save()
        return instance