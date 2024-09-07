from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name

