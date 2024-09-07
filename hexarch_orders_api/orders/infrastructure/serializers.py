from rest_framework import serializers
from .models import OrderModel, OrderItemModel

class OrderItemSerializer(serializers.ModelSerializer):
    reference = serializers.CharField()

    class Meta:
        model = OrderItemModel
        fields = ['reference', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    created_at = serializers.DateTimeField()

    class Meta:
        model = OrderModel
        fields = ['id', 'items', 'total_price_without_tax', 'total_price_with_tax', 'created_at']
