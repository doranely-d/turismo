from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel
from .validators import validate_file_size 
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager

__all__ = ['Configuration', 'Video']


class Configuration(SingletonModel):
    title = models.CharField(_('title'), max_length=255)
    subtitle = models.CharField(_('sub title'), max_length=255)
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    excerpt = models.TextField(_('excerpt'))
    description = RichTextUploadingField(_('description'))
    banner_image = models.ImageField(
        _('banner image'), upload_to='asomarte_banner', validators=[validate_file_size])
    web_site = models.URLField(_('web site'), max_length=255, blank=True)
    magazine_image = models.ImageField(
        _('magazine image'), upload_to='asomarte_magazines', blank=True, validators=[validate_file_size])
    magazine_image_alt_text = models.CharField(
        _('Alt text'), max_length=255, blank=True)
    magazine_url = models.URLField(
        _('magazine url'), max_length=255, blank=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Configuration')
        # translate = (
        #     'title', 'subtitle', 'excerpt', 'description',
        #     'meta_description', 'meta_keywords', 'magazine_image_alt_text',
        # )

    def __str__(self):
        return u'Configuration'

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_magazine_image_url(self):
        if self.magazine_image:
            return self.magazine_image.url
        return ''


class Video(models.Model):
    title = models.CharField(_('title'), max_length=255)
    link = models.URLField(_('Link'), max_length=255)
    blank = models.BooleanField(
        _('Target Blank'), default=False,
        help_text=_('Open link in another tab')
    )
    excerpt = models.TextField(_('Excerpt'))
    image = models.ImageField(_('Image'), upload_to='videos', max_length=255, validators=[validate_file_size])
    image_alt_text = models.CharField(
        _('Alt text'), max_length=255, blank=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
        # translate = ('title', 'excerpt', 'image_alt_text',)

    def __str__(self):
        return u'%s' % self.title

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''
