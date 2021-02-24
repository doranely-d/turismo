from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url

from . import views


urlpatterns = [
    url(_(r'^visitors/$'), views.landing, name='landing'),
    url(_(r'^visitors-guide/$'), views.visitors_guide, name='visitors_guide'),
]
