from qa.views import application
import django
if django.VERSION[0] > 3:
  from django.urls import include, re_path
else:
  from django.conf.urls import url, include


if django.VERSION[0] > 3:
    urlpatterns = [
    re_path(r'^$', application, name='main'),
    re_path(r'^login\/$', application, name='login'),
    re_path(r'^signup/$', application, name='signup'),
    re_path(r'^ask/$', application, name='ask'),
    re_path(r'^popular/$', application, name='popular'),
    re_path(r'^new/$', application, name='new'),
    re_path(r'^question/(\d+)/$', application, name='question')
  ]
else:
   urlpatterns = [
    url(r'^$', application, name='main'),
    url(r'^login\/$', application, name='login'),
    url(r'^signup/$', application, name='signup'),
    url(r'^ask/$', application, name='ask'),
    url(r'^popular/$', application, name='popular'),
    url(r'^new/$', application, name='new'),
    url(r'^question/(\d+)/$', application, name='question')
  ]
