from rest_framework import serializers
from .models import ItemModel

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'

    def create(self, validated_data):
        return ItemModel.objects.create(**validated_data)


# from rest_framework import serializers

# class ItemSerializer(serializers.Serializer):
#     reference = serializers.CharField(max_length=100)
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=255)
#     price_without_tax = serializers.FloatField()
#     tax = serializers.FloatField()
#     created_at = serializers.DateTimeField(read_only=True)
