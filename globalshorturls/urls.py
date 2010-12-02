# encoding: utf-8
from django.conf.urls.defaults import *

urlpatterns = patterns('globalshorturls.views',
    url(r'^$', 'index', name='globalshorturls.index'),
    url(r'^deleteshorturl/(?P<url_id>\d+)/$', 'delete_shorturl', name='globalshorturls.delete_shorturl'),
    # You may want to move the following to the end of the global urls.py
    url(r'^(?P<shorturl>[a-zA-Z0-9]+)/$', 'globalshorturls.views.redirect', name='globalshorturls.redirect')
)
