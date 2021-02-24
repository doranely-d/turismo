from django.utils.translation import ugettext_lazy as _
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel
from django.urls import reverse
from .validators import validate_file_size 
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager

__all__ = ['Category', 'Configuration', 'Post']


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'))
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    slug = models.SlugField(_('slug'), max_length=255)
    thumbnail_image = models.ImageField(
        _('thumbnail image'),
        upload_to='thumbnail_categories_posts', validators=[validate_file_size]
    )
    thumbnail_image_alt_text = models.CharField(
        _('Alt text'), max_length=255, blank=True)
    banner_image = models.ImageField(
        _('banner image'),
        upload_to='banner_categories_posts', validators=[validate_file_size]
    )

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        # translate = (
        #     'name', 'slug', 'description', 'meta_description', 'meta_keywords',
        #     'thumbnail_image_alt_text',
        # )

    def __str__(self):
        return u'%s' % self.name

    # @models.permalink
    def absolute_url(self):
        return reverse('Blog:category', args=[self.id, self.slug])

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_thumbnail_image_url(self):
        if self.thumbnail_image:
            return self.thumbnail_image.url
        return ''


class Configuration(SingletonModel):
    outstanding_post = models.OneToOneField(
        'Post',
        verbose_name=_('Outstanding Post'),
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    categories_title = models.CharField(
        _('Header of Featured Articles'), max_length=255)
    category_title = models.CharField(_('Categories Header'), max_length=255)
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Configuration')
        # translate = (
        #     'categories_title', 'category_title', 'meta_description', 'meta_keywords',
        # )

    def __str__(self):
        return u'Configuration'


class Post(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    subtitle = models.CharField(_('sub title'), max_length=255)
    excerpt = models.TextField(_('excerpt'))
    meta_description = models.CharField(
        _('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    content = RichTextUploadingField(_('content'))
    banner_image = models.ImageField(
        _('banner image'), upload_to='banner_posts', validators=[validate_file_size]
    )
    post_image = models.ImageField(_('Content Image'), upload_to='posts', validators=[validate_file_size])
    post_image_alt_text = models.CharField(
        _('Alt text'), max_length=255, blank=True)
    category = models.ForeignKey(
        'Category',
        related_name='posts',
        verbose_name=_('category'),
        on_delete=models.CASCADE
    )
    featured = models.BooleanField(_('Featured'), default=False)
    publish_date = models.DateField(_('publish date'))
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        # translate = (
        #     'title', 'slug', 'subtitle', 'excerpt', 'content',
        #     'meta_description', 'meta_keywords', 'post_image_alt_text',
        # )
        ordering = ['-id']

    def __str__(self):
        return u'%s' % self.title

    # @models.permalink
    def absolute_url(self):
        return reverse('Blog:post', args=[self.id, self.slug])

    def get_search_title(self):
        return self.title

    def get_search_category(self):
        return self.category.name

    def get_search_description(self):
        return self.excerpt

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return ''

    def get_post_image_url(self):
        if self.post_image:
            return self.post_image.url
        return ''
