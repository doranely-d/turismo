from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url

from . import views
from .models import Card
from Blog.models import Post
from Events.models import Event
from Regions.models import Section


urlpatterns = [
    url(_(r'^what-to-do/(?P<category_id>\d+)/(?P<slug>[\w\-]+)/$'), views.landing, name='landing'),
    url(_(r'^what-to-do/section/(?P<section_id>\d+)/(?P<slug>[\w\-]+)/$'), views.section, name='section'),
    url(_(r'^what-to-do/card/(?P<card_id>\d+)/(?P<slug>[\w\-]+)/$'), views.card, name='card'),
    # Search
    url(_(r'^search/$'), views.search, name='search'),
    url(_(r'^search/category/(?P<category_id>\d+)/$'), views.search, {'model':Card}, name='search_category'),
    url(_(r'^search/event/$'), views.search, {'model':Event}, name='search_event'),
    url(_(r'^search/post/$'), views.search, {'model':Post}, name='search_post'),
    url(_(r'^search/section/$'), views.search, {'model':Section}, name='search_section'),
]
