from django.db import models

from django.conf import settings
from django.core.files.storage import default_storage
import os
#from .model import Category

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    stock=models.IntegerField(default=0)
    price=models.FloatField(default=0.0)
    rating=models.FloatField(default=0.0)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='media')
    barcode = models.CharField(max_length=100, null=True, blank=True)
    #category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.pk and self.img.name != 'default.jpeg':
            old_product = Product.objects.get(pk=self.pk)
            full_img_path = os.path.join(settings.MEDIA_ROOT, 'default.jpeg')
            if old_product.img.path != self.img.path and old_product.img.path != full_img_path:
                default_storage.delete(old_product.img.path)
        super().save(*args, **kwargs)