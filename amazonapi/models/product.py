from django.db import models
from .user import User


class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
