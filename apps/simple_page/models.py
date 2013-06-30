# -*- coding: utf-8 -*-

from django.db import models
from pay2pay.models import Payment


class Order(models.Model):
    name = models.CharField('ФИО', max_length=128)
    address = models.CharField('Адрес', max_length=246)
    email = models.EmailField('Email')
    payment = models.ForeignKey(Payment, verbose_name='Платеж', blank=True, null=True)
    sent = models.BooleanField('Отправлен')
    created = models.DateTimeField('Создан', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'заказы'


class Video(models.Model):
    name = models.CharField('Название', max_length=128)
    code = models.CharField('Код видео', max_length=16)
    show = models.BooleanField('Показывать', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('show',)
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'