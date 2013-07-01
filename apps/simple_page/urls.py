# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import HomePage
from .views import MakeOrder

urlpatterns = patterns('',
    url(r'^$', HomePage.as_view(), name='home_page'),
    url(r'^make-order/$', MakeOrder.as_view(), name='order_make'),
)