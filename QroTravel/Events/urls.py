from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from django.conf.urls import url

from . import views


urlpatterns = [
    url(_(r'^events/$'), views.landing, name='landing'),
    url(_(r'^events/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$'), views.landing, name='month_landing'),
    url(_(r'^events/(?P<event_id>\d+)/(?P<slug>[\w\-]+)/$'), views.event, name='event'),
]
