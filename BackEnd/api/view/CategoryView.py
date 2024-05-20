from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import generics , permissions, status
from api.model.CategoryModel import "modelo"
from api.serializers.CategorySerializer import "traerserializador"



class CategoryListCreate(generics.ListCreateApiView):
    pass