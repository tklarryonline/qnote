from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qnote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include('qnote_api.urls')),

    url(r'^', include('qnote_web.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
