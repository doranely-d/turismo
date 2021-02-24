from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    # Admin Site URLs
    url(r'^admin/', admin.site.urls),
    url(r'^robots\.txt', include('robots.urls')),
    url(r'^', include('QroTravel.urls_sitemaps')),
    # Internacionalization
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Ckeditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    # CMS URLs
    url(r'^', include( ('CMS.urls','CMS'), namespace='CMS')),
    # Asomarte URLs
    url(r'^', include( ('Asomarte.urls','Asomarte'), namespace='Asomarte')),
    # Blog URLs
    url(r'^', include( ('Blog.urls','Blog'), namespace='Blog')),
    # Events
    url(r'^', include( ('Events.urls','Events'), namespace='Events')),
    # FAQ
    url(r'^', include(('FAQ.urls','FAQ'), namespace='FAQ')),
    # Gastronomy
    url(r'^', include(('Gastronomy.urls','Gastronomy'), namespace='Gastronomy')),
    # Regions
    url(r'^', include(('Regions.urls','Regions'), namespace='Regions')),
    # Visitor
    url(r'^', include(('Visitor.urls','Visitor'), namespace='Visitor')),
    # Whats hot
    url(r'^', include(('WhatsHot.urls','WhatsHot'), namespace='WhatsHot')),
    #Configuration URLs
    url(r'^', include(('Configuration.urls','Configuration'), namespace='Configuration')),
)


if settings.DEBUG:
    urlpatterns += static('/mediafiles/', document_root=settings.MEDIA_ROOT, show_indexes=True)
    urlpatterns += static('/staticfiles/', document_root=settings.STATIC_ROOT, show_indexes=True)
