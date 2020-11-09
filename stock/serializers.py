from rest_framework import serializers
from stock.models import Stock
from django.contrib.auth.models import User


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            'id',
            'user_id',
            'ingredient_id',
            'amount',
            'expiration_date',
        )
        read_only_fields = ('id', )