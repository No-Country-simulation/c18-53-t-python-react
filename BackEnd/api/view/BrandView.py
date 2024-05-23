from rest_framework import viewsets, permissions, serializers

from api.model.BrandModel import Brand
from api.serializers.BrandSerializer import BrandSerializer

class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BrandSerializer