# -*- coding: utf-8 -*-

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        exclude = ('sent', 'payment', 'created')
        model = Order