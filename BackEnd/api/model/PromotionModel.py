from django.db import models
from api.model.ProductModel import Product

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    ending_date = models.DateTimeField()
    products = models.ManyToManyField(Product)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name