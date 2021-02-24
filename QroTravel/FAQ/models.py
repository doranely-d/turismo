from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.templatetags.static import static

from solo.models import SingletonModel
from django.urls import reverse
from .validators import validate_file_size 
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager


__all__ = ['Category', 'Question', 'Configuration']


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        # translate = ('name', 'slug',)
        ordering =('name',)

    def __str__(self):
        return u'%s' % self.name

    # @models.permalink
    def absolute_url(self):
        return reverse('FAQ:faq_category', args=[self.id, self.slug])


class Configuration(SingletonModel):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('sub title'))
    meta_description = models.CharField(_('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    banner_image = models.ImageField(_('Banner Image'), upload_to='contact', validators=[validate_file_size])

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Configuration')
        # translate = ('title', 'description', 'meta_description', 'meta_keywords',)

    def __unicode__(self):
        return u'Configuration'

    def get_banner_image_url(self):
        if self.banner_image:
            return self.banner_image.url
        return static('img/banner_default.jpg')


class Question(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    answer = models.TextField(_('Answer'))
    display = models.BooleanField(_('Display'), default=True)
    order = models.PositiveIntegerField(_('Order'), default=0)
    category = models.ForeignKey(
        'Category',
        verbose_name=_('Category'),
        related_name='questions',
        on_delete=models.CASCADE)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        # translate = ('title', 'answer')
        ordering = ('order', 'title')

    def __unicode__(self):
        return u'%s' % self.title
