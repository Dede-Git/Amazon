from django.db import models
from .user import User


class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(max_length=100)
    price = models.IntegerField(max_length=50)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
