from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import translation
from django.conf import settings

from .models import *

from datetime import datetime

__all__ = ['EventsSitemap']


class EventsSitemap(Sitemap):
    changefreq = "always"

    def items(self):
        items_arr = ['Events:landing']
        items_arr_final = []
        for lang_code, lang in settings.LANGUAGES:
            translation.activate(lang_code)
            for item in items_arr:
                items_arr_final.append(reverse(item))
        items = list(Event.objects.all())
        for lang_code, lang in settings.LANGUAGES:
            translation.activate(lang_code)
            for item in items:
                items_arr_final.append(item.absolute_url())
        initial_year = 2017
        for lang_code, lang in settings.LANGUAGES:
            translation.activate(lang_code)
            for year in range(initial_year, datetime.now().year + 2):
                for month in range(1, 13):
                    items_arr_final.append(
                        reverse('Events:month_landing', args=[year, str(month).zfill(2)])
                    )
        return items_arr_final

    def location(self, item):
        return item
