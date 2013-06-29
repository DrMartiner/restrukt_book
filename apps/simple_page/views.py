# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from apps.simple_page.models import Video


class HomePage(TemplateView):
    template_name = 'simple_page/home_page.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['videos'] = Video.objects.filter(show=True)
        return ctx


class OrderSuccess(TemplateView):
    template_name = 'simple_page/order_success.html'


class OrderFail(TemplateView):
    template_name = 'simple_page/order_fail.html'