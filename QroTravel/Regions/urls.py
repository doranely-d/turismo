from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url

from . import views


urlpatterns = [
    url(_(r'^regions/$'), views.landing, name='landing'),
    url(_(r'^region/(?P<region_id>\d+)/(?P<slug>[\w\-]+)/$'), views.region, name='region'),
    url(_(r'^section/(?P<section_id>\d+)/(?P<slug>[\w\-]+)/$'), views.section, name='section'),
]
