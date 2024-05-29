from django.db import models
from .ProductModel import Product

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    ending_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name