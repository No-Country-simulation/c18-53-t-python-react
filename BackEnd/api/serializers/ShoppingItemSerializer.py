from rest_framework import serializers, viewsets
from .models import Shopping, ShoppingItem, Product
from user.models import User


class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ['product', 'quantity']