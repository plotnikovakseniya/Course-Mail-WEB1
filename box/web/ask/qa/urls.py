from qa.views import application
from django.urls import re_path, include

urlpatterns = [
	re_path(r'^$', application, name='main'),
	re_path(r'^login\/$', application, name='login'),
        re_path(r'^signup/$', application, name='signup'),
        re_path(r'^ask/$', application, name='ask'),
        re_path(r'^popular/$', application, name='popular'),
        re_path(r'^new/$', application, name='new'),
	re_path(r'^question/(?P<pk>\d+)/$', application, name='question')
]
