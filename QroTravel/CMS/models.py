from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

from solo.models import SingletonModel
from .validators import validate_file_size 
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager


__all__ = ['Category', 'ContactGroup', 'Contact', 'Inspiration', 'Slide']


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255)
    order = models.PositiveSmallIntegerField(_('order'), default=0)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        # translate = ('name',)
        ordering = ['order']

    def __str__(self):
        return u'%s' % self.name


class ContactGroup(models.Model):
    category = models.ForeignKey(
        'Category',
        verbose_name=_('category'),
        related_name='contacts',
        on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=255)
    phone = models.CharField(_('phone'), max_length=15, blank=True)
    toll_free = models.CharField(_('toll free'), max_length=20, blank=True)
    web_site = models.URLField(_('web site'), blank=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Contact Group')
        verbose_name_plural = _('Contacts Group')
        # translate = ('name',)
        ordering = ['name']

    def __str__(self):
        return u'%s' % self.name


class Contact(SingletonModel):
    title = models.CharField(_('Title'), max_length=255)
    excerpt = models.TextField(_('sub title'))
    description = models.TextField(_('Description'))
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    banner_image = models.ImageField(_('Banner Image'), upload_to='contact', validators=[validate_file_size])
    address = models.TextField(_('Address'))
    web_site = models.CharField(_('Web Site'), blank=True, max_length=255)
    contact_email = models.EmailField(_('Contact Email'), blank=True)
    instagram_url = models.URLField(
        _('Instagram url'), max_length=255, blank=True)
    twitter_url = models.URLField(_('Twitter url'), max_length=255, blank=True)
    facebook_url = models.URLField(
        _('Facebook url'), max_length=255, blank=True)
    phone_1 = models.CharField(_('Phone 1'), max_length=15, blank=True)
    phone_2 = models.CharField(_('Phone 2'), max_length=15, blank=True)
    phone_3 = models.CharField(_('Phone 3'), max_length=15, blank=True)
    google_maps = models.TextField(_('Google Maps Iframe'), blank=True, help_text=_(
        'Visit maps.google.com and copy the iframe'))

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Contact')
        # translate = (
        #     'title', 'excerpt', 'description', 'meta_description', 'meta_keywords',
        # )

    def __str__(self):
        return u'Contact'

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''


class Inspiration(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    link = models.URLField(_('Link'), max_length=255)
    blank = models.BooleanField(
        _('Target Blank'), default=False,
        help_text=_('Open link in another tab')
    )
    image = models.ImageField(_('Image'), upload_to='inspiration', validators=[validate_file_size])
    image_alt_text = models.CharField(
        _('Alt text'), max_length=255, blank=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Inspiration')
        verbose_name_plural = _('Inspirations')
        # translate = ('title', 'image_alt_text',)

    def __str__(self):
        return u'%s' % self.title

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


class Slide(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    link = models.URLField(_('Link'), max_length=255)
    blank = models.BooleanField(
        _('Target Blank'), default=False,
        help_text=_('Open link in another tab')
    )
    banner_image = models.ImageField(_('Banner Image'), upload_to='banners', validators=[validate_file_size])
    button_image_white = models.ImageField(
        _('Button icon white'), upload_to='banners', blank=True, validators=[validate_file_size])
    button_image_color = models.ImageField(
        _('Button icon color'), upload_to='banners', blank=True, validators=[validate_file_size])
    order = models.PositiveSmallIntegerField(_('Order'), default=0)
    display = models.BooleanField(_('Display'), default=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')
        # translate = ('title',)
        ordering = ['order']

    def __str__(self):
        return u'%s' % self.title

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_button_image_white_url(self):
        if self.button_image_white:
            return self.button_image_white.url
        return ''

    def get_button_image_color_url(self):
        if self.button_image_color:
            return self.button_image_color.url
        return ''
