from rest_framework import serializers, viewsets
from serializers.ShoppingSerializer import ShoppingSerializer
from model.ShoppingModel import Shopping

class ShoppingViewSet(viewsets.ModelViewSet):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer