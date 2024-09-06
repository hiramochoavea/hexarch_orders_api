from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import OrderModel, OrderItemModel
from hexarch_orders_api.items.infrastructure.models import ItemModel
from hexarch_orders_api.items.infrastructure.serializers import ItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    reference = serializers.CharField()
    #reference = serializers.CharField(source='item.reference')

    class Meta:
        model = OrderItemModel
        fields = ['reference', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = ['id', 'items', 'total_price_without_tax', 'total_price_with_tax', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        #print(items_data)
        order = OrderModel.objects.create(**validated_data)
        
        for item_data in items_data:
            reference = item_data.get('reference')
            item = get_object_or_404(ItemModel, reference=reference)
            
            quantity = item_data.get('quantity', 0)
            if quantity:
                OrderItemModel.objects.create(order=order, item=item, quantity=quantity)
        
        return order