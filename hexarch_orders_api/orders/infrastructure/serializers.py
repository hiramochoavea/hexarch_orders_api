from rest_framework import serializers
from .models import OrderModel

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'

    def create(self, validated_data):
        return OrderModel.objects.create(**validated_data)