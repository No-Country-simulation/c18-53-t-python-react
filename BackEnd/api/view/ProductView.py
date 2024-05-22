from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import generics , permissions, status

from rest_framework import viewsets
from api.model.ProductModel import Product
from api.serializers.ProductSerializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer