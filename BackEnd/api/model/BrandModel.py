from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    #description = models.TextField()
    img = models.ImageField(upload_to='img_brand')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name