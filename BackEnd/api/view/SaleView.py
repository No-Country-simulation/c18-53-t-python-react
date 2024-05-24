from rest_framework import viewsets, permissions, serializers

from api.model.SaleModel import Sale
from api.serializers.SaleSerializer import SaleSerializer

class SaleViewSet(viewsets.ModelViewSet):

    queryset = Sale.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SaleSerializer