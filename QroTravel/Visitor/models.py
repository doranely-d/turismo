from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.conf import settings
from django.db import models

from .utils import season_types, transportation_types

from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel
from .validators import validate_file_size 
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager



__all__ = [
    'Configuration', 'QueretaroLanding', 'QueretaroSection', 'Season',
    'Section', 'TransportationType',
]


class Configuration(SingletonModel):
    # Landing
    title = models.CharField(_('Title'), max_length=255)
    section_name = models.CharField(_('Section name'), max_length=255)
    subtitle = models.TextField(_('Description'))
    meta_description = models.CharField(_('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    banner_image = models.ImageField(
        _('Banner image'), upload_to='visitor_banner', validators=[validate_file_size]
    )
    # Location
    location_description = models.TextField(_('Location description'))
    sub_heading = RichTextUploadingField(_('Sub Heading'), blank=True)
    sub_heading_title = models.CharField(
        _('Sub Heading Title'), max_length=255, blank=True
    )
    location_image = models.ImageField(
        _('Location image'), upload_to='visitor_location', validators=[validate_file_size]
    )
    # How to arrive
    arrive_description = models.TextField(_('Arrive description'))
    background_arrive_image = models.ImageField(
        _('Background arrive image'), upload_to='visitor_arrive_background', validators=[validate_file_size]
    )
    # Weather
    weather_description = models.TextField(
        _('Weather description'), blank=True
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Visitor Guide Configuration')
        # translate = (
        #     'title', 'subtitle', 'location_description', 'sub_heading', 'section_name',
        #     'arrive_description', 'weather_description', 'sub_heading_title',
        #     'meta_description', 'meta_keywords',
        # )

    def __str__(self):
        return u'Visitor Guide Configuration'

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_location_image_url(self):
        if self.location_image:
            return self.location_image.url
        return ''

    def get_background_arrive_image_url(self):
        if self.background_arrive_image:
            return self.background_arrive_image.url
        return ''


class QueretaroLanding(SingletonModel):
    title = models.CharField(_('Title'), max_length=255)
    excerpt = models.TextField(_('sub title'))
    meta_description = models.CharField(_('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    banner_image = models.ImageField(
        _('Image of the Queretaro banner'), upload_to='queretaro_landing_banner', validators=[validate_file_size]
    )
    heading = models.TextField(_('Location description'))
    description = models.TextField(_('Sub Heading'))
    image = models.ImageField(_('Location image'), upload_to='visitor_location', validators=[validate_file_size])
    faqs_text = RichTextUploadingField(_('FAQs text'), blank=True)
    show_faqs_text = models.BooleanField(_('Show faqs text'))

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Queretaro Landing')
        # translate = (
        #     'title', 'excerpt', 'heading', 'description', 'faqs_text',
        #     'meta_description', 'meta_keywords',
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


class QueretaroSection( models.Model):
    title = models.CharField(_('Title'), max_length=255)
    sub_title = RichTextUploadingField(_('Sub Title'))
    excerpt = RichTextUploadingField(_('Excerpt'))
    banner_image = models.ImageField(
        _('Banner image'), upload_to='queretaro_section_banner', validators=[validate_file_size]
    )
    order = models.PositiveSmallIntegerField(_('order'), default=0)
    # Button
    button_text = models.CharField(_('button text'), max_length=255, blank=True)
    button_link = models.CharField(_('button link'), max_length=255, blank=True)
    blank = models.BooleanField(
        _('Target Blank'), default=False,
        help_text=_('Open link in another tab')
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Queretaro Section')
        verbose_name_plural = _('Queretaro Sections')
        ordering = ('order',)
        # translate = (
        #     'title', 'sub_title', 'excerpt', 'button_text', 'button_link',
        # )

    def __str__(self):
        return u'%s' % self.title

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''


class Season(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))
    icon = models.CharField(
        _('Icon'), max_length=40, choices=season_types.SEASON_TYPE_CHOICES,
        default=season_types.WINTER
    )
    image = models.ImageField(_('Image'), upload_to='visitor_seasons', validators=[validate_file_size])

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Visitor Guide Season')
        verbose_name_plural = _('Visitor Guide Seasons')
        # translate = ('title', 'description',)

    def __str__(self):
        return u'%s' % self.title

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


class Section(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    sub_title = models.TextField(_('Sub Title'))
    heading = models.CharField(_('Heading'), max_length=255)
    sub_heading = RichTextUploadingField(_('Sub Heading'))
    banner_image = models.ImageField(
        _('Banner image'), upload_to='visitor_section_banner', validators=[validate_file_size]
    )
    section_file = models.FileField(
        _('Section file'), upload_to='visitor_section_file',
        blank=True, null=True
    )
    button_section_text = models.CharField(
        _('Button Section Text'), max_length=255, blank=True
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Visitor Guide Section')
        verbose_name_plural = _('Visitor Guide Sections')
        # translate = (
        #     'title', 'sub_title', 'sub_heading', 'heading',
        #     'button_section_text'
        # )

    def __str__(self):
        return u'%s' % self.title

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_section_file_url(self):
        if self.section_file:
            return self.section_file.url
        return ''


class TransportationType(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))
    icon = models.CharField(
        _('Icon'), max_length=40,
        choices=transportation_types.TRANSPORTATION_TYPE_CHOICES,
        default=transportation_types.AIRPLANE
    )
    image = models.ImageField(
        _('Image'), upload_to='visitor_transportation_types', validators=[validate_file_size]
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Visitor Guide Transportation Type')
        verbose_name_plural = _('Visitor Guide Transportation Types')
        # translate = ('title', 'description',)

    def __str__(self):
        return u'%s' % self.title

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''
