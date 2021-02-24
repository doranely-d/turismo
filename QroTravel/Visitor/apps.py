from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class VisitorConfig(AppConfig):
    name = 'Visitor'
    verbose_name = _('Visitor')
