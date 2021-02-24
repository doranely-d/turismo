from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url

from . import views


urlpatterns = [
    url(_(r'^blog/$'), views.categories, name='categories'),
    url(_(r'^blog/(?P<category_id>\d+)/(?P<slug>[\w\-]+)/$'), views.category, name='category'),
    url(_(r'^blog/post/(?P<post_id>\d+)/(?P<slug>[\w\-]+)/$'), views.post, name='post'),
]
