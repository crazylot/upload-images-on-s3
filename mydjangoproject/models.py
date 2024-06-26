from django.db import models

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    name = models.CharField(max_length=255)
    photo = models.FileField()

    def __str__(self):
        return self.name
    