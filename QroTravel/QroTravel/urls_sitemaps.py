from django.contrib.sitemaps import views as sitemaps_views
from django.conf.urls import url

from Asomarte.sitemaps import *
from Blog.sitemaps import *
from CMS.sitemaps import *
from Configuration.sitemaps import *
from Events.sitemaps import *
from FAQ.sitemaps import *
from Gastronomy.sitemaps import *
from Regions.sitemaps import *
from Visitor.sitemaps import *
from WhatsHot.sitemaps import *


sitemaps = {
    'asomarte': AsomarteSitemap,
    'blog': BlogSitemap,
    'cms': CMSSitemap,
    'configuration': ConfigurationSitemap,
    'events': EventsSitemap,
    'faq': FAQSitemap,
    'gastronomy': GastronomySitemap,
    'regions': RegionsSitemap,
    'visitor': VisitorSitemap,
    'whatshot': WhatsHotSitemap,
}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemaps_views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap, {'sitemaps': sitemaps}),
]
