from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'riddles.views.home_page', name='home'),

    # url(r'^admin/', include(admin.site.urls)),
)
