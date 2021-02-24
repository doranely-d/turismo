from django.utils.translation import ugettext_lazy as _
from django.db import models

# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager

from lib.managers import DisplayManager
from .validators import validate_file_size 

import os

__all__ = ['ExternalLink', 'FooterLink', 'FooterSubLink']


class ExternalLink(models.Model):
    name = models.CharField(_('name'), max_length=255)
    image = models.FileField(_('icon'), upload_to=os.path.join('images', 'footer'), help_text=_('Color svg file'))
    url = models.URLField(_('link url'), max_length=255, blank=True)
    order = models.PositiveSmallIntegerField(_('order'), default=0)
    display = models.BooleanField(_('display'), default=True)

    # Managers
    objects = DisplayManager()

    class Meta:
        verbose_name = _('Footer Logo Link')
        verbose_name_plural = _('Footer Logo Links')
        ordering = ('order',)

    def __str__(self):
        return u'%s' % self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


class FooterLink(models.Model):
    title = models.CharField(_('title'), max_length=255)
    link = models.CharField(_('link'), max_length=255, blank=True)
    order = models.PositiveSmallIntegerField(_('order'), default=0)
    active = models.BooleanField(_('active'), default=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Footer Link')
        verbose_name_plural = _('Footer Links')
        # translate = ('title', 'link',)
        ordering = ('order',)

    def __str__(self):
        return u'%s' % self.title


class FooterSubLink(models.Model):
    main_menu_link = models.ForeignKey(
        'FooterLink',
        related_name='sublinks',
        verbose_name=_('main menu link'),
        on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=255)
    link = models.CharField(_('link'), max_length=255)
    new_window = models.BooleanField(_('open in new window'), default=False)
    order = models.PositiveSmallIntegerField(_('order'), default=0)
    active = models.BooleanField(_('active'), default=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Footer SubLink')
        verbose_name_plural = _('Footer SubLinks')
        # translate = ('title', 'link',)
        ordering = ('order',)

    def __str__(self):
        return u'%s' % self.title
