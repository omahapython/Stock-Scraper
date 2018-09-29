from rest_framework import serializers
from stock_api.apps.daily_prices.models import DailyPrices

class DailyPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrices
        fields = '__all__'