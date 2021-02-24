from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.conf import settings
from django.db import models


from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager


__all__ = ['GastronomyLanding', 'GastronomySection']


class GastronomyLanding(SingletonModel):
    title = models.CharField(_('Title'), max_length=255)
    excerpt = models.TextField(_('sub title'))
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    banner_image = models.ImageField(
        _('Banner image'), upload_to='gastronomy_landing_banner'
    )
    heading = models.TextField(_('Location description'))
    description = models.TextField(_('Sub Heading'))
    image = models.ImageField(
        _('Location image'), upload_to='gastronomy_location')
    image_alt_text = models.CharField(
        _('Alt text'), max_length=255, blank=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Gastronomy Landing')
        # translate = (
        #     'title', 'excerpt', 'heading', 'description',
        #     'meta_description', 'meta_keywords', 'image_alt_text'
        # )

    def __str__(self):
        return u'Queretaro Landing'

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


class GastronomySection(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    sub_title = RichTextUploadingField(_('Sub Title'))
    excerpt = RichTextUploadingField(_('Excerpt'))
    banner_image = models.ImageField(
        _('Banner image'), upload_to='gastronomy_section_banner'
    )
    order = models.PositiveSmallIntegerField(_('order'), default=0)
    # Button
    button_text = models.CharField(
        _('button text'), max_length=255, blank=True)
    link = models.CharField(_('Link'), max_length=255, blank=True)
    blank = models.BooleanField(
        _('Target Blank'), default=False,
        help_text=_('Open link in another tab')
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Gastronomy Section')
        verbose_name_plural = _('Gastronomy Sections')
        ordering = ('order',)
        # translate = (
        #     'title', 'sub_title', 'excerpt', 'button_text',
        # )

    def __str__(self):
        return u'%s' % self.title

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''
