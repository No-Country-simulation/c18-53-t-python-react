from django.db import models
from user.models import User
from api.model.ProductModel import Product


class Shopping(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE) # Eliminar tabla
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name.first_name}" 
    

