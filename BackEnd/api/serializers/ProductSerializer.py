from rest_framework import serializers
from api.model.ProductModel import Product

from api.model.CategoryModel import Category
from api.model.BrandModel import Brand

class ProductSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model= Product
        # fields = '__all__'
        fields = ['id','name','description','stock','price','rating','status','img','barcode','category_id','branding']

    