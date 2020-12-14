from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, default="Item Title")
    description = models.CharField(max_length=800, blank=False, null=False, default="Item Description")
    price = models.FloatField(blank=False, null=False, default=0.0)
    picture = models.ImageField(blank=True)


class ItemFeatures(models.Model):
    feature = models.CharField(max_length=200, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
