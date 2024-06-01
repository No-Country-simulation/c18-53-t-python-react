from rest_framework import serializers, permissions, viewsets

from api.model.CategoryModel import Category
from api.serializers.CategorySerializer import CategorySerializer

from rest_framework.parsers import MultiPartParser, FormParser

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, FormParser]
