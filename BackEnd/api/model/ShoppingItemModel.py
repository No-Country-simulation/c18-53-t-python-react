from django.db import models
from .ShoppingModel import Shopping
from .ProductModel import Product


class ShoppingItem(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product