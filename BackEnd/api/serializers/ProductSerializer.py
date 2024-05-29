from rest_framework import serializers
from api.model.ProductModel import Product

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        # fields = '__all__'
        fields = ['name','description','stock','price','rating','status','img','barcode']

