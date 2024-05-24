from rest_framework import viewsets, permissions, serializers

from api.model.SaleDetailModel import SaleDetail
from api.serializers.SaleDetailSerializer import SaleDetailSerializer

class SaleDetailViewSet(viewsets.ModelViewSet):

    queryset = SaleDetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SaleDetailSerializer