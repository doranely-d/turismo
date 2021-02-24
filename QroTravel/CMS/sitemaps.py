from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import translation
from django.conf import settings

from .models import *

__all__ = ['CMSSitemap']


class CMSSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        items_arr = ['CMS:index', 'CMS:contact']
        items_arr_final = []
        for lang_code, lang in settings.LANGUAGES:
            translation.activate(lang_code)
            for item in items_arr:
                items_arr_final.append(reverse(item))
        return items_arr_final

    def location(self, item):
        return item
