from rest_framework import serializers, viewsets
from .ShoppingItemSerializer import ShoppingItemSerializer
from model.ShoppingModel import Shopping
from model.ShoppingItemModel import ShoppingItem

class ShoppingSerializer(serializers.ModelSerializer):
    items = ShoppingItemSerializer(many=True)

    class Meta:
        model = Shopping
        fields = ['user', 'items', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        shopping = Shopping.objects.create(**validated_data)
        for item_data in items_data:
            ShoppingItem.objects.create(shopping=shopping, **item_data)
        return shopping