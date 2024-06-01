from django.db import models

from django.conf import settings
from django.core.files.storage import default_storage
import os

class Brand(models.Model):
    name = models.CharField(max_length=100)
    #description = models.TextField()
    img = models.ImageField(upload_to='img_brand')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk and self.img.name != 'default.jpeg':
            old_brand = Brand.objects.get(pk=self.pk)
            full_img_path = os.path.join(settings.MEDIA_ROOT, 'default.jpeg')
            if old_brand.img.path != self.img.path and old_brand.img.path != full_img_path:
                default_storage.delete(old_product.img.path)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
