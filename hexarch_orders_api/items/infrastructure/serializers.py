from rest_framework import serializers
from .models import ItemModel


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for converting ItemModel instances to and from JSON.

    Attributes:
        price_without_tax (FloatField): The price of the item excluding tax.
        tax (FloatField): The applicable tax rate for the item.
    """

    price_without_tax = serializers.FloatField()
    tax = serializers.FloatField()

    class Meta:
        model = ItemModel
        fields = '__all__'
