from rest_framework import serializers
from .models import ItemModel

class ItemSerializer(serializers.ModelSerializer):
    price_without_tax = serializers.FloatField()
    tax = serializers.FloatField()    
    class Meta:
        model = ItemModel
        fields = '__all__'