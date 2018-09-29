from django.db import models
from stock_api.apps.tickers.models import Ticker

class DailyPrices(models.Model):

    symbol = models.ForeignKey(Ticker, on_delete=models.CASCADE, to_field='symbol')
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()

