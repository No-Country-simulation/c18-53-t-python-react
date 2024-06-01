from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import generics , permissions, status

from rest_framework import viewsets
from api.model.ProductModel import Product
from api.serializers.ProductSerializer import ProductSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.parsers import MultiPartParser, FormParser

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(img=self.request.data.get('img'))


    @swagger_auto_schema(tags=["Productos"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Productos"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Productos"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Productos"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Productos"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Productos"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    