# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'show')
    list_editable = ('name', 'show')


admin.site.register(Video, VideoAdmin)