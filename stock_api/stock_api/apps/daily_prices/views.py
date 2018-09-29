from rest_framework import viewsets
from .models import DailyPrices
from .serializers import DailyPricesSerializer


class DailyPricesViewSet(viewsets.ModelViewSet):

    queryset = DailyPrices.objects.all()
    serializer_class = DailyPricesSerializer
