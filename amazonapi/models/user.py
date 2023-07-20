from django.db import models


class User(models.Model):

    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    isseller = models.BooleanField(default=False)
