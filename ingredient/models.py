from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    trim = models.TextField(default="")
    keep = models.TextField(default="")
    buy = models.TextField(default="")
