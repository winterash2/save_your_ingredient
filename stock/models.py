from django.db import models
from ingredient.models import Ingredient
from django.contrib.auth.models import User


AMOUNT_CHOICES = [
    ('많음', '많음'),
    ('보통', '보통'),
    ('적음', '적음'),
]


class Stock(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(
        max_length=2,
        choices=AMOUNT_CHOICES,
        default='많음',
    )
    expiration_date = models.DateField(auto_now_add=True)
