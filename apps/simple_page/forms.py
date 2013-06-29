# -*- coding: utf-8 -*-

from django import forms


class OrderForm(forms.ModelForm):

    class Meta:
        exclude = ('pub_date', 'is_pay')