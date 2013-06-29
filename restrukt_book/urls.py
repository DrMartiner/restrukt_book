# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from apps.simple_page.views import HomePage
from apps.simple_page.views import OrderFail
from apps.simple_page.views import OrderSuccess

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePage.as_view(), name='home_page'),
    url(r'^fail/$', OrderFail.as_view(), name='order_fail'),
    url(r'^success/$', OrderSuccess.as_view(), name='order_success'),
    url(r'^djangojs/', include('djangojs.urls')),
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