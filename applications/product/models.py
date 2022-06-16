from tabnanny import verbose
from unicodedata import decimal
from django.db import models
from django.contrib.auth import get_user_model

from applications.category.models import Category

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=80, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=20, decimal_places=3, verbose_name='Price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Product')
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    logo = models.ImageField(blank=True, null=True, upload_to='images', default="images/2-500x500_iwW2IIp.jpeg")

    def __str__(self) -> str:
        return self.title
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')

    def __str__(self):
        return self.product.title
    
    