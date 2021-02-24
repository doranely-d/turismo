from django.utils.translation import ugettext_lazy as _
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel
from django.urls import reverse
from .validators import validate_file_size 
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager

__all__ = [
    'Card', 'CardPhoto', 'CategoryFilter', 'CategoryFilterOption',
    'Category', 'Section', 'Keyword',
]


class Card(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    meta_description = models.CharField(_('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    subtitle = RichTextUploadingField(_('sub title'), max_length=255)
    subheading = models.CharField(_('sub heading'), max_length=255)
    excerpt = models.TextField(
        _('excerpt'),
        help_text=_(
            'Excerpt to display on search results and short descriptions'
        )
    )
    description = RichTextUploadingField(_('description'))
    #image = models.ImageField(_('image'), upload_to='cards')
    image = models.ImageField(_('image'), upload_to='cards', validators=[validate_file_size])
    address = models.TextField(_('Address'), blank=True)
    web_site = models.CharField(_('Web Site'), blank=True, max_length=255)
    contact_email = models.EmailField(_('Contact Email'), blank=True)
    instagram_url = models.URLField(
        _('Instagram url'), max_length=255, blank=True
    )
    twitter_url = models.URLField(_('Twitter url'), max_length=255, blank=True)
    facebook_url = models.URLField(
        _('Facebook url'), max_length=255, blank=True
    )
    phone = models.CharField(_('Phone'), max_length=15, blank=True)
    phone_2 = models.CharField(_('Phone 2'), max_length=15, blank=True)
    phone_3 = models.CharField(_('Phone 3'), max_length=15, blank=True)
    google_maps = models.TextField(
        _('Google Maps Iframe'), blank=True,
        help_text=_('Visit maps.google.com and copy the iframe')
    )
    link = models.URLField(_('Link'), max_length=255, blank=True)
    blank = models.BooleanField(
        _('Target Blank'), default=False,
        help_text=_('Open link in another tab')
    )
    button_text = models.CharField(
        _('button text'), max_length=255, blank=True
    )
    # 360 View
    button_360_link = models.URLField(
        _('Button 360 Link'), max_length=255, blank=True
    )
    button_360_text = models.CharField(
        _('button 360 text'), max_length=255, blank=True
    )
    # Many To Many Keys
    sections = models.ManyToManyField(
        'Section', related_name='cards', verbose_name=_('sections'),
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        related_name='cards',
        verbose_name=_('category'),
        blank=True,
        on_delete=models.CASCADE
    )
    category_filters = models.ManyToManyField(
        'CategoryFilterOption', related_name='cards',
        verbose_name=_('category filters'), blank=True,
    )
    # Created
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    # Keywords
    keywords = models.ManyToManyField(
        'Keyword', related_name='cards', verbose_name=_('keywords'),
        blank=True
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')
        # translate = (
        #     'title', 'subtitle', 'description', 'button_text', 'subheading',
        #     'slug', 'excerpt', 'button_360_text', 'meta_description', 'meta_keywords',
        # )
        ordering = ('title',)

    def __str__(self):
        return u'%s' % self.title

    # @models.permalink
    def absolute_url(self):
        return reverse('WhatsHot:card', args=[self.id, self.slug])

    def get_search_title(self):
        return self.title

    def get_search_category(self):
        try:
            return self.category.name
        except:
            aux = []
            qs = self.sections.select_related('main_category').all()
            for q in qs:
                name = q.main_category.name
                if name not in aux:
                    aux.append(name)
            return ', '.join(aux)
        return ''

    def get_search_description(self):
        return self.excerpt

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


class CardPhoto(models.Model):
    image = models.ImageField(_('image'), upload_to='whatshot_card_photos', validators=[validate_file_size])
    section = models.ForeignKey(
        'Card',
        verbose_name=_('Card'),
        related_name='card_photos',
        on_delete=models.CASCADE
    )
    order = models.PositiveSmallIntegerField(_('order'), default=0)

    class Meta:
        verbose_name = _('Card Photo')
        verbose_name_plural = _('Card Photos')
        ordering = ('order',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


class CategoryFilter(models.Model):
    name = models.CharField(_('name'), max_length=255)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Category Filter')
        verbose_name_plural = _('Category Filters')
        # translate = ('name',)
        ordering = ('name',)

    def __str__(self):
        return u'%s' % self.name


class CategoryFilterOption(models.Model):
    category_filter = models.ForeignKey(
        'CategoryFilter',
        related_name='options',
        verbose_name=_('category filter'),
        on_delete=models.CASCADE
    )
    name = models.CharField(_('name'), max_length=255)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Category Filter Option')
        verbose_name_plural = _('Category Filter Options')
        # translate = ('name',)
        ordering = ('order',)

    def __str__(self):
        return u'%s' % self.name


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    title = models.CharField(_('title'), max_length=255)
    description = models.CharField(_('description'), max_length=255)
    meta_description = models.CharField(_('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    banner_image = models.ImageField(_('banner image'), upload_to='cat_banner_image', validators=[validate_file_size])
    has_sections = models.BooleanField(_('has sections'), default=True)
    filters = models.ManyToManyField(
        'CategoryFilter', blank=True, verbose_name=_('category filter'),
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        # translate = (
        #     'title', 'name', 'description', 'slug', 'meta_description', 'meta_keywords',
        # )
        ordering = ('name',)

    def __str__(self):
        return u'%s' % self.name

    # @models.permalink
    def absolute_url(self):
        return reverse('WhatsHot:landing', args=[self.id, self.slug])

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''


class Section(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.CharField(_('slug'), max_length=255)
    description = models.CharField(_('sub title'), max_length=255)
    meta_description = models.CharField(_('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    image = models.ImageField(_('image'), upload_to='sections', validators=[validate_file_size])
    main_category = models.ForeignKey(
        'Category',
        related_name='main_sections',
        verbose_name=_('main category'),
        on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(
        'Category', related_name='sections', verbose_name=_('category'),
        blank=True
    )
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    outstanding = models.BooleanField(_('Outstanding'), default=False)
    banner_image = models.ImageField(
        _('banner image'), upload_to='sec_banner_image', validators=[validate_file_size]
    )
    order = models.PositiveSmallIntegerField(_('Order'), default=0)
    category_filters = models.ManyToManyField(
        'CategoryFilterOption', related_name='sections',
        verbose_name=_('category filters'), blank=True,
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Section WH')
        verbose_name_plural = _('Sections WH')
        # translate = (
        #     'title', 'description', 'slug', 'meta_description', 'meta_keywords',
        # )
        ordering = ('order',)

    def __str__(self):
        return u'%s' % self.title

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''

    # @models.permalink
    def absolute_url(self):
        return reverse('WhatsHot:section', args=[self.id, self.slug])

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''


class Keyword(models.Model):
    name = models.CharField(_('name'), max_length=255)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Keyword')
        verbose_name_plural = _('Keywords')
        # translate = ('name',)
        ordering = ['name']

    def __str__(self):
        return u'%s' % self.name
