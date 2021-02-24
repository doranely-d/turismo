from django.utils.translation import ugettext_lazy as _
from django.template import defaultfilters
from django.utils import translation
from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel
from django.urls import reverse
from .validators import validate_file_size 
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager


__all__ = ['Configuration', 'Region', 'Section', 'SectionPhoto']


class Configuration(SingletonModel):
    # Landing
    title = models.CharField(_('Title'), max_length=255)
    subtitle = models.TextField(_('sub title'))
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    banner_image = models.ImageField(
        _('Banner image'), upload_to='regions_banner', validators=[validate_file_size]
    )
    # Regions General Data
    sub_regions_sub_heading = models.TextField(
        _('Sub Regions Sub Heading'), blank=True
    )
    sub_regions_heading = models.TextField(
        _('Sub Regions Heading'), blank=True
    )
    sub_regions_image = models.ImageField(
        _('Sub Regions image'), upload_to='sub_regions_image', validators=[validate_file_size]
    )
    sub_regions_image_alt_text = models.CharField(
        _('Alt text'), max_length=255, blank=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Region Guide Configuration')
        # translate = (
        #     'title', 'subtitle', 'sub_regions_heading',
        #     'sub_regions_sub_heading', 'meta_description', 'meta_keywords',
        #     'sub_regions_image_alt_text',
        # )

    def __str__(self):
        return u'Regions Configuration'

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_sub_regions_image_url(self):
        if self.sub_regions_image:
            return self.sub_regions_image.url
        return ''


class Region(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    title_color = models.CharField(
        _('Title Color'), max_length=7,
        help_text=_('Hexadecimal color #000000')
    )
    sub_title = RichTextUploadingField(_('Inner Banner Subtitle'))
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    heading = RichTextUploadingField(_('Heading'))
    sub_heading = RichTextUploadingField(_('Sub Heading'))
    extra_data = RichTextUploadingField(_('Extra Data'))
    banner_image = models.ImageField(
        _('Banner image'), upload_to='region_banner', validators=[validate_file_size]
    )
    sub_banner_image = models.ImageField(
        _('Sub Banner image'), upload_to='sub_region_banner', validators=[validate_file_size]
    )
    sub_banner_image_alt_text = models.CharField(
        _('Alt text'), max_length=255, blank=True)
    # Button
    button_text = models.CharField(
        _('button text'), max_length=255, blank=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')
        # translate = (
        #     'title', 'slug', 'sub_title', 'sub_heading', 'heading',
        #     'extra_data', 'button_text', 'meta_description', 'meta_keywords',
        #     'sub_banner_image_alt_text',
        # )

    def __str__(self):
        return u'%s' % self.title

    # @models.permalink
    def absolute_url(self):
        return reverse('Regions:region', args=[self.id, self.slug])

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_sub_banner_image_url(self):
        if self.sub_banner_image:
            return self.sub_banner_image.url
        return ''


class Section(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    sub_title = RichTextUploadingField(_('Sub Title'))
    sub_heading = RichTextUploadingField(_('Sub Heading'))
    banner_image = models.ImageField(
        _('Banner image'), upload_to='region_section_banner', validators=[validate_file_size]
    )
    excerpt = models.TextField(
        _('excerpt'),
        help_text=_(
            'Excerpt to display on search results and short descriptions')
    )
    content = RichTextUploadingField(_('content'), blank=True)
    address = models.TextField(_('Address'), blank=True)
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
    # Foreign Key
    region = models.ManyToManyField('Region', related_name='sections')
    # Button
    button_text = models.CharField(
        _('button text'), max_length=255, blank=True)
    link = models.CharField(_('Link'), max_length=255, blank=True)
    blank = models.BooleanField(
        _('Target Blank'), default=False,
        help_text=_('Open link in another tab')
    )
    # Ordering
    order = models.PositiveSmallIntegerField(_('order'), default=0)
    # Created
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Regions Section')
        verbose_name_plural = _('Regions Sections')
        # translate = (
        #     'title', 'slug', 'sub_title', 'sub_heading', 'button_text',
        #     'content', 'excerpt', 'meta_description', 'meta_keywords',
        # )
        ordering = ('order',)

    def __str__(self):
        return u'%s' % self.title

    # @models.permalink
    def absolute_url(self):
        return reverse('Regions:section', args=[self.id, self.slug])
    

    def get_search_title(self):
        return self.title

    def get_search_category(self):
        aux = []
        qs = self.region.all()
        for q in qs:
            name = q.title
            if name not in aux:
                aux.append(name)
        return ', '.join(aux)

    def get_search_description(self):
        if self.excerpt:
            return defaultfilters.safe(self.excerpt)
        if self.sub_heading:
            return defaultfilters.safe(self.sub_heading)
        if self.region.sub_heading:
            return defaultfilters.safe(self.region.sub_heading)
        return _('No information available')

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''


class SectionPhoto(models.Model):
    image = models.ImageField(_('image'), upload_to='region_section_photos', validators=[validate_file_size])
    alt_text = models.CharField(_('Alt text'), max_length=255, blank=True)
    section = models.ForeignKey(
        'Section',
        verbose_name=_('Section'),
        related_name='section_photos',
        on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(_('order'), default=0)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Section Photo')
        verbose_name_plural = _('Section Photos')
        ordering = ('order',)
        # translate = ('alt_text',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''
