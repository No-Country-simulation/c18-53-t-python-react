from django.db import models
from user.models import User


class Shopiping(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    
class ShoppingItem(models.Model):
    shopping = models.ForeignKey(Shopiping, on_delete=models.CASCADE)
    product = models.ForeignKey()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product