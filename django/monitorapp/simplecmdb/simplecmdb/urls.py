from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/gethosts\.json$','hostinfo.views.gethosts'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^api/collect$','hostinfo.views.collect'),
    url(r'^api/monitor_collect$','hostinfo.views.monitor_collect'),
    url(r'^monitor_list/$','hostinfo.views.monitor_list'),
    url(r'^tq_list/$','hostinfo.views.tq_list'),
    url(r'^api/tq_collect$','hostinfo.views.tq_collect'),
    # Examples:
    # url(r'^$', 'simplecmdb.views.home', name='home'),
    # url(r'^simplecmdb/', include('simplecmdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
