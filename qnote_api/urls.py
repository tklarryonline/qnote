'''
Created by tklarryonline on May 21, 2014.
'''
from django.conf.urls import patterns, include, url
from qnote_api.views.quote_view import QuoteView


urlpatterns = patterns('',
    url(r'^quotes/$', QuoteView.as_view(), name='qnote_api_quotes'),
)