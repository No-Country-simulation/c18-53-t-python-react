from rest_framework import viewsets, permissions, serializers

from api.model.BrandModel import Brand
from api.serializers.BrandSerializer import BrandSerializer

from rest_framework.parsers import MultiPartParser, FormParser


class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = BrandSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(img=self.request.data.get('img'))