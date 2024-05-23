from rest_framework import serializers, permissions, viewsets

from api.model.CategoryModel import Category
from api.serializers.CategorySerializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
