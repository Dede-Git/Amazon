from django.db import models
from .user import User


class Order(models.Model):

    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    closed = models.BooleanField(default=False)
