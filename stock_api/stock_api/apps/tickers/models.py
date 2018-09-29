from django.db import models

class Ticker(models.Model):

    symbol = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return self.symbol