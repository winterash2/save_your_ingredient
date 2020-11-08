from django.db import models
from ingredient.models import Ingredient


class Stock(models.Model):
    ingredient_id = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    amount = models.TextField()
    expiration_date = models.DateField(auto_now_add=True)
