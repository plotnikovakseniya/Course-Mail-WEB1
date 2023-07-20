from qa.views import application
from django.conf.urls import url, include
# from django.urls import include

urlpatterns = [
	url(r'^$', application, name='main'),
	url(r'^login\/$', application, name='login'),
        url(r'^signup/$', application, name='signup'),
        url(r'^ask/$', application, name='ask'),
        url(r'^popular/$', application, name='popular'),
        url(r'^new/$', application, name='new'),
	url(r'^question/(\d+)/$', application, name='question')
]
