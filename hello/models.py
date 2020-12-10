from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    rating = models.IntegerField()