from rest_framework import serializers, viewsets
from serializers.ShoppingSerializer import ShoppingSerializer
from model.ShoppingModel import Shopping

from rest_framework.parsers import MultiPartParser, FormParser

class ShoppingViewSet(viewsets.ModelViewSet):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer
    parser_classes = [MultiPartParser, FormParser]