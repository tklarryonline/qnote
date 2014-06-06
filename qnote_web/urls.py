'''
Created by tklarryonline on Jun 05, 2014.
'''
from django.conf.urls import patterns, url
from qnote_web.views.index_view import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='qnote_web_index'),
)
