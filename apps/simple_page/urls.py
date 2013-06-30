# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import HomePage
from .views import MakeOrder
from .views import OrderFail
from .views import OrderSuccess

urlpatterns = patterns('',
    url(r'^$', HomePage.as_view(), name='home_page'),
    url(r'^make-order/$', MakeOrder.as_view(), name='order_make'),
    url(r'^fail/$', OrderFail.as_view(), name='order_fail'),
    url(r'^success/$', OrderSuccess.as_view(), name='order_success'),
)