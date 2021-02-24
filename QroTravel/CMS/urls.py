from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url, include

from . import views


urlpatterns = [
    # Index
    url(r'google091eb2281440ab65.html', views.google),
    url(r'^$', views.index, name='index'),
    url(_(r'^contact/$'), views.contact, name='contact'),
]
