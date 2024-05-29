from rest_framework import serializers
from api.model.SaleModel import Sale

class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ['user_name','sale_date','total']
