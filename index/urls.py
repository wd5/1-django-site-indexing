from django.conf.urls import patterns, include, url
from index.models import Site

urlpatterns = patterns('index.views',
    url(r'^$', 'list'),
    url(r'^page/(?P<page_slug>[-\w]+)/$', 'page'),
    url(r'^site/(?P<site_id>\d+)/$', 'view'),
    url(r'^click/(?P<site_id>\d+)/$', 'click'),
    url(r'^stats/$', 'stats'),
)
