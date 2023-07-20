from qa.views import application
import django
if django.VERSION[0] > 3:
  from django.urls import re_path, include
  urlfunc = re_path
else:
  from django.conf.urls import url, include
  urlfunc = url

urlpatterns = [
    urlfunc(r'^$', application, name='main'),
    urlfunc(r'^login\/$', application, name='login'),
    urlfunc(r'^signup/$', application, name='signup'),
    urlfunc(r'^ask/$', application, name='ask'),
    urlfunc(r'^popular/$', application, name='popular'),
    urlfunc(r'^new/$', application, name='new'),
    urlfunc(r'^question/(\d+)/$', application, name='question')
]
