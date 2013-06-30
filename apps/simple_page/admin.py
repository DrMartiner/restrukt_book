# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Video
from .models import Order


class VideoAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'show')
    list_editable = ('name', 'show')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'sent', 'address', 'email_html', 'created')
    list_filter = ('sent', 'created', 'payment__status')
    search_fields = ('name', 'address')

    def email_html(self, obj):
        return '<a href="mailto:{0}">{0}</a>'.format(obj.email)

admin.site.register(Video, VideoAdmin)
admin.site.register(Order, OrderAdmin)