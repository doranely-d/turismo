from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url

from . import views


urlpatterns = [
    url(_(r'^gastronomy/$'), views.landing, name='landing'),
]
