# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Video
from .models import Order


class VideoAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'show')
    list_editable = ('name', 'show')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'sent', 'status', 'address', 'email_html', 'created')
    list_filter = ('sent', 'created', 'payment__status')
    list_editable = ('sent',)
    search_fields = ('name', 'address')
    ordering = ('-sent', 'created')

    readonly_fields = ('name', 'address', 'email', 'payment')

    def email_html(self, obj):
        return '<a href="mailto:{0}">{0}</a>'.format(obj.email)
    email_html.allow_tags = True
    email_html.short_description = 'Email'

    def status(self, obj):
        return obj.payment.get_status_display()
    status.allow_tags = True
    status.short_description = 'Статус платежа'

admin.site.register(Video, VideoAdmin)
admin.site.register(Order, OrderAdmin)