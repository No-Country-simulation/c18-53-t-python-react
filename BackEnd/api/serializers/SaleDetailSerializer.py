from rest_framework import serializers
from api.model.SaleDetailModel import SaleDetail

class SaleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleDetail
        # fields = '__all__'
        fields = ['quantity','unit_price']
