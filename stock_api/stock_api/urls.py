"""stock_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

# app urls
from stock_api.apps.tickers import views as ticker_views
from stock_api.apps.daily_prices import views as daily_views


router = DefaultRouter()
router.register(r'stocks_followed', ticker_views.TickerViewSet)
router.register(r'daily_prices', daily_views.DailyPricesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include(router.urls))
]
