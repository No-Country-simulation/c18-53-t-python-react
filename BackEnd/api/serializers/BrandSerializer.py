from rest_framework import serializers
from api.model.BrandModel import Brand

class BrandSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Brand
        # fields = '__all__'
        fields = ['id','name','img']
