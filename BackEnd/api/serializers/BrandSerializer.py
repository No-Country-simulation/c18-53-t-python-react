from rest_framework import serializers
from api.model.BrandModel import Brand

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'