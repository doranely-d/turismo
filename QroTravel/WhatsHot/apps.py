from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class WhatshotConfig(AppConfig):
    name = 'WhatsHot'
    verbose_name = _("What's Hot")
