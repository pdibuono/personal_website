from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^contact/create/$', ContactCreateView.as_view(), name='contact_create'),
    url(r'^success/$', Success.as_view(), name='success'),
    url(r'^aboutme/$', AboutMeView.as_view(), name='aboutme'),
    url(r'^contact_info/$', ContactInfoView.as_view(), name='contact_info'),
)