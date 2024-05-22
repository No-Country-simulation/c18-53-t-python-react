from django.db import models
#from .model import Category

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    stock=models.IntegerField(default=0)
    price=models.FloatField(default=0.0)
    rating=models.FloatField(default=0.0)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='definir ruta')
    barcode = models.CharField(max_length=100, null=True, blank=True)
    #category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now=True)