from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import translation
from django.conf import settings

from .models import *

__all__ = ['BlogSitemap']


class BlogSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        items_arr = ['Blog:categories']
        items_arr_final = []
        for lang_code, lang in settings.LANGUAGES:
            translation.activate(lang_code)
            for item in items_arr:
                items_arr_final.append(reverse(item))
        items = list(Category.objects.all()) + list(Post.objects.all())
        for lang_code, lang in settings.LANGUAGES:
            translation.activate(lang_code)
            for item in items:
                items_arr_final.append(item.absolute_url())
        return items_arr_final

    def location(self, item):
        return item
