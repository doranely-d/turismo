from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static
from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager
from solo.models import SingletonModel
from .validators import validate_file_size 

__all__ = ['Category', 'Configuration', 'Event', 'EventPhoto']


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        # translate = ('name',)
        ordering = ('order',)

    def __str__(self):
        return u'%s' % self.name


class Configuration(SingletonModel):
    title = models.CharField(_('title'), max_length=255)
    excerpt = models.TextField(_('sub title'))
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    banner_image = models.ImageField(
        _('banner image'), upload_to='events_configuration', validators=[validate_file_size])

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Configuration')
        # translate = ('title', 'excerpt', 'meta_description', 'meta_keywords',)

    def __str__(self):
        return u'%s' % _('Configuration')

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''


class Event( models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    subtitle = models.CharField(_('subtitle'), max_length=255)
    excerpt = models.TextField(_('excerpt'))
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    content = RichTextUploadingField(_('content'))
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))
    image = models.ImageField(_('image'), upload_to='events', validators=[validate_file_size])
    image_alt_text = models.CharField(
        _('Alt Text'), max_length=255, blank=True)
    banner_image = models.ImageField(
        _('banner image'), upload_to='banner_events', validators=[validate_file_size])
    address = RichTextUploadingField(_('Address'))
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
    published = models.BooleanField(_('Published'), default=False)
    category = models.ForeignKey(
        'Category',
        related_name='events',
        verbose_name=_('category'),
        on_delete=models.CASCADE)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        # translate = (
        #     'title', 'slug', 'subtitle', 'excerpt', 'content',
        #     'meta_description', 'meta_keywords', 'image_alt_text',
        # )

    def __str__(self):
        return u'%s' % self.title

    # @models.permalink
    def absolute_url(self):
        return reverse('Events:event', args=[self.id, self.slug])

    def get_search_title(self):
        return self.title

    def get_search_category(self):
        return '%s - %s' % (_('Event'), self.category.name)

    def get_search_description(self):
        return self.excerpt

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''


class EventPhoto( models.Model):
    image = models.ImageField(_('image'), upload_to='event_photos', validators=[validate_file_size])
    event = models.ForeignKey(
        'Event',
        verbose_name=_('Event'),
        related_name='event_photos',
        on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(_('order'), default=0)
    alt_text = models.CharField(_('Alt text'), max_length=255, blank=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('EventPhoto')
        verbose_name_plural = _('Event Photos')
        ordering = ('order',)
        # translate = ('alt_text',)

    def __str__(self):
        return u'%s' % self.id

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''
