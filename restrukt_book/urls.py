# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('apps.simple_page.urls')),
    url(r'^djangojs/', include('djangojs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^pay2pay/', include('pay2pay.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml', TemplateView.as_view(template_name='sitemao.xml', content_type='text/xml')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )
else:
    urlpatterns += patterns('',
        url(r'^admin/', include('admin_honeypot.urls')),
        url(r'^admin.php', include('admin_honeypot.urls')),
        url(r'^admin-secret/', include(admin.site.urls)),
    )