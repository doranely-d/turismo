from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^aviso-de-privacidad/', views.privacy_policy, name='privacy_policy'),
    url(r'^transparencia/', views.transparency, name='transparency'),
]
