from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# from linguo.models import MultilingualModel
# from linguo.managers import MultilingualManager
from solo.models import SingletonModel
from .validators import validate_file_size 

__all__ = ['Home']

SITE_NAME = getattr(settings, 'SITE_NAME', '')


class Home(SingletonModel):
    google_analytics = models.CharField(_('Google Analytics'), max_length=15, blank=True, help_text='UA-XXXXX-X')
    meta_description = models.CharField(_('Meta Description'), max_length=255, blank=True)
    meta_keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    promotions = models.URLField(_('Promotions'), max_length=255, blank=True)
    reserve = models.URLField(_('Reserve'), max_length=255, blank=True)
    occ = models.URLField(_('Occ'), max_length=255, blank=True)
    discover = models.TextField(_('Discover'), blank=True, help_text=_('embed code'))
    # Social ULRs
    instagram_url = models.URLField(_('instagram url'), max_length=255, blank=True)
    facebook_url = models.URLField(_('facebook url'), max_length=255, blank=True)
    twitter_url = models.URLField(_('twitter url'), max_length=255, blank=True)
    # Contact
    contact_email = models.EmailField(_('Contact Email'), blank=True)
    # Temperature
    min_temp = models.CharField(_('min temperature'), max_length=255, blank=True)
    max_temp = models.CharField(_('max temperature'), max_length=255, blank=True)
    weather_icon = models.CharField(_('weather icon'), max_length=10, blank=True)
    # Search Configuration
    search_title = models.CharField(_('Search title'), max_length=255, blank=True)
    search_subtitle = models.CharField(_('Search subtitle'), max_length=255, blank=True)
    search_banner_image = models.ImageField(_('Search banner Image'), upload_to='configuration_images', blank=True, validators=[validate_file_size])
    # Error page configuration
    error_banner_image = models.ImageField(_('Error banner Image'), upload_to='configuration_images', blank=True, validators=[validate_file_size])
    # Privacy policy
    privacy_policy_banner_image = models.ImageField(_('Privacy policy banner Image'), upload_to='configuration_images', blank=True, validators=[validate_file_size])
    privacy_policy = RichTextUploadingField(_('privacy policy'), blank=True)
    # Transparency policy
    transparency_banner_image = models.ImageField(_('Transparency banner Image'), upload_to='transparency_images', blank=True, validators=[validate_file_size])
    transparency = RichTextUploadingField(_('Transparency'), blank=True)

    # Managers
    # objects = MultilingualManager()

    class Meta:
        verbose_name = 'Configuration'
        # translate = (
        #     'search_title', 'search_subtitle', 'privacy_policy', 'transparency',
        #     'meta_description', 'meta_keywords',
        # )

    def __str__(self):
        return u'Configuration %s' % SITE_NAME

    def has_social_urls(self):
        social_urls = [
            self.instagram_url,
            self.twitter_url,
            self.facebook_url,
        ]
        return any(social_urls)

    def get_weather_icon(self):
        if self.weather_icon:
            return self.weather_icon
        return '01d'

    def get_search_banner_image_url(self):
        if self.search_banner_image:
            return self.search_banner_image.url
        return ''

    def get_error_banner_image_url(self):
        if self.error_banner_image:
            return self.error_banner_image.url
        return ''

    def get_privacy_policy_banner_image_url(self):
        if self.privacy_policy_banner_image:
            return self.privacy_policy_banner_image.url
        return ''

    def get_transparency_banner_image_url(self):
        if self.transparency_banner_image:
            return self.transparency_banner_image.url
        return ''
