from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    rating = models.IntegerField()