from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^asomarte/$', views.landing, name='landing'),
]
