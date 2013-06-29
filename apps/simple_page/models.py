# -*- coding: utf-8 -*-

from django.db import models


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