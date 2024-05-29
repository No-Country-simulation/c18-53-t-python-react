from django.db import models
from user.models import User
from api.model.ProductModel import Product


class Shopping(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    
class ShoppingItem(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product