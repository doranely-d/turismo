from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^faqs/$', views.landing, name='landing'),
    url(r'^faqs/(?P<category_id>\d+)/(?P<slug>[\w\-]+)/$', views.faq_category, name='faq_category'),
]
