from rest_framework import viewsets, permissions, serializers

from api.model.SaleDetailModel import SaleDetail
from api.serializers.SaleDetailSerializer import SaleDetailSerializer

from rest_framework.parsers import MultiPartParser, FormParser
class SaleDetailViewSet(viewsets.ModelViewSet):

    queryset = SaleDetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SaleDetailSerializer
    parser_classes = [MultiPartParser, FormParser]
