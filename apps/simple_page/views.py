# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from .forms import OrderForm
from constance import config
from pay2pay.models import Payment
from .models import Video


class HomePage(TemplateView):
    template_name = 'simple_page/home_page.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['videos'] = Video.objects.filter(show=True)
        return ctx


class MakeOrder(FormView):
    form_class = OrderForm

    def form_invalid(self, form):
        errors = {}
        for name in form.fields:
            error = form.errors.get(name)
            if error:
                errors[name] = error[0]
        return HttpResponse(json.dumps(errors), status=200, mimetype='application/json')

    def form_valid(self, form):
        payment = Payment(
            amount=config.SHOP_ORDER_AMOUNT,
            description=config.SHOP_ORDER_DESCIPTION
        )
        payment.save()

        order = form.save()
        order.payment = payment
        order.save()

        pay_data = {
            'xml': payment.xml.encode('base64'),
            'sign': payment.signature,
        }

        return HttpResponse(json.dumps(pay_data), status=201, mimetype='application/json')