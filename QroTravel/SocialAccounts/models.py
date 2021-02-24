from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.conf import settings
from django.db import models

from solo.models import SingletonModel

from .utils import feeds_types

from datetime import datetime
from dateutil import parser
from .validators import validate_file_size 

import facebook
import requests
import twitter
import json


__all__ = ['Feed', 'FacebookConfiguration', 'FacebookAccount', 'InstagramAccount', 'TwitterAccount']


class FacebookConfiguration(SingletonModel):
    client_id = models.CharField(_('Client ID'), max_length=255)
    app_secret_key = models.CharField(_('App Secret Key'), max_length=255)

    class Meta:
        verbose_name = _('Facebook App Configuration')

    def __unicode__(self):
        return u'%s' % _('Facebook App Configuration')


class FacebookAccount(models.Model):
    display_name = models.CharField(_('Display Name'), max_length=255, help_text=_('Display name on this page.'))
    screen_name = models.CharField(_('Screen Name'), max_length=255, help_text=_('Facebook page name, found in URL'))

    class Meta:
        verbose_name = _('Facebook Account')
        verbose_name_plural = _('Facebook Accounts')

    def __unicode__(self):
        return u'%s' % self.display_name

    def load_posts(self):
        translation.activate('es')
        try:
            token_url = getattr(settings, 'FACEBOOK_GRAPH_URL', '')
            fb_config = FacebookConfiguration.objects.get()
            if not token_url:
                return
            params = dict(client_id=fb_config.client_id, client_secret=fb_config.app_secret_key, grant_type='client_credentials')
            token_response = requests.get(url=token_url, params=params)
            access_token = token_response.text.split('=')[1]
            graph = facebook.GraphAPI(access_token)
            query_string = 'posts?limit={0}'.format(10)
            profile = graph.get_object(self.screen_name)
            posts = graph.get_connections(profile['id'], query_string)
            for post in posts.get('data'):
                post_id = post.get('id', '')
                # MEDIA URL IF IT HAS ONE
                media_url = ''
                try:
                    media_response = graph.get_connections(id=post_id, connection_name='attachments')
                    media_data = media_response.get('data')
                    media_first = media_data[0]
                    if media_first.get('type', '') == 'photo':
                        media_img = media_first.get('media').get('image')
                        media_url = media_img.get('src', '')
                    elif media_first.get('type', '') == 'album':
                        media_subattachments_data = media_first.get('subattachments').get('data')
                        media_subattachments_first = media_subattachments_data[0]
                        media_img = media_subattachments_first.get('media').get('image')
                        media_url = media_img.get('src', '')
                except:
                    pass
                # PARSE ORIGINAL PUBLICATION DATE
                publish_date = datetime.now()
                try:
                    publish_date = post.get('created_time', '').split('+')[0]
                except:
                    pass
                feeds, created = Feed.objects.get_or_create(uid=post_id, defaults={
                    'title': self.display_name.upper(),
                    'content': post.get('message', ''),
                    'feeds_type': feeds_types.FACEBOOK,
                    'media_url': media_url,
                    'publish_date': publish_date,
                })
        except Exception as e:
            print ('ERROR Loading Facebook Posts: %s' % e)


class Feed(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    account_display_name = models.CharField(_('Account display name'), max_length=255, blank=True)
    profile_img = models.URLField(_('Profile image'), blank=True)
    content = models.TextField(_('Content'), blank=True)
    image = models.ImageField(_('Image'), upload_to='feeds', blank=True, validators=[validate_file_size])
    media_url = models.URLField(_('Media Url'), blank=True)
    link = models.CharField(_('Link'), max_length=255, blank=True)
    blank = models.BooleanField(
        _('Target Blank'), default=False,
        help_text=_('Open link in another tab')
    )
    feeds_type = models.CharField(
        _('Feeds type'), max_length=20, choices=feeds_types.FEEDS_TYPE_CHOICES,
        default=feeds_types.FACEBOOK
    )
    uid = models.CharField(_('Uid'), max_length=255, blank=True)
    publish_date = models.DateTimeField(_('Publish Date'), blank=True, null=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Feed')
        verbose_name_plural = _('Feeds')
        ordering = ['-publish_date']

    def get_profile_image(self):
        if self.profile_img:
            return self.profile_img
        return ''

    def get_image_url(self):
        if self.image:
            return self.image.url
        if self.media_url:
            return self.media_url
        return ''

    def __unicode__(self):
        return u'%s' % self.title


class InstagramAccount(models.Model):
    display_name = models.CharField(_('Display Name'), max_length=255, help_text=_('Display name on this page.'))
    access_token = models.CharField(_('access token'), max_length=255)


    class Meta:
        verbose_name = _('Instagram Account')
        verbose_name_plural = _('Instagram Accounts')

    def __unicode__(self):
        return u'%s' % self.display_name

    def load_posts(self):
        translation.activate('es')
        try:
            media_url = getattr(settings, 'INSTAGRAM_GRAPH_URL', '')
            if not media_url:
                return
            media_url = media_url.format(self.access_token)
            media_response = requests.get(url=media_url)
            posts = media_response.json()
            if media_response.status_code != 200:
                return
            for post in posts.get('data'):
                post_id = post.get('id', '')
                # MEDIA URL IF IT HAS ONE
                image_url = ''
                try:
                    image_url = post['images']['standard_resolution']['url']
                except:
                    pass
                # PARSE ORIGINAL PUBLICATION DATE
                publish_date = datetime.now()
                try:
                    publish_date = post.get('created_time', '')
                    publish_date = datetime.fromtimestamp(float(publish_date)).strftime("%Y-%m-%d %H:%M")
                except Exception:
                    pass
                content = ''
                try:
                    content = post['caption']['text']
                except Exception:
                    pass
                link = ''
                try:
                    link = post['link']
                except Exception:
                    pass
                try:
                    feed, created = Feed.objects.get_or_create(uid=post_id, defaults={
                        'title': self.display_name.upper(),
                        'content': content,
                        'link': link,
                        'feeds_type': feeds_types.INSTAGRAM,
                        'media_url': image_url,
                        'publish_date': publish_date,
                    })
                except:
                    continue
        except Exception as e:
            print ('ERROR Loading Instagram Posts: %s' % e)


class TwitterAccount(models.Model):
    display_name = models.CharField(_('Display Name'), max_length=255, help_text=_('Display name on this page.'))
    username = models.CharField(_('Twitter Username'), max_length=255)
    oauth_token = models.CharField(_('OAuth Token'), max_length=255)
    oauth_secret = models.CharField(_('OAuth Secret'), max_length=255)
    twitter_key = models.CharField(_('Twitter Key'), max_length=255)
    twitter_key_secret = models.CharField(_('Twitter Key Secret'), max_length=255)

    class Meta:
        verbose_name = _('Twitter Account')
        verbose_name_plural = _('Twitter Accounts')

    def __unicode__(self):
        return u'%s' % self.display_name

    def load_posts(self):
        translation.activate('es')
        auth = twitter.oauth.OAuth(
            self.oauth_token, self.oauth_secret,
            self.twitter_key, self.twitter_key_secret
        )
        statuses = []
        try:
            twitter_api = twitter.Twitter(auth=auth)
            statuses = twitter_api.statuses.user_timeline(screen_name=self.username)[:10]
            for twit in statuses:
                r = json.dumps(twit)
                twit = json.loads(r)
                twit_id = twit.get('id', '')
                # MEDIA URL IF IT HAS ONE
                media_url = ''
                try:
                    media = twit['entities']['media']
                    media = json.dumps(media[0])
                    media = json.loads(media)
                    media_url = media['media_url_https']
                except:
                    pass
                profile_img = ''
                try:
                    profile_img = twit['user']['profile_image_url_https']
                except:
                    pass
                # PARSE ORIGINAL PUBLICATION DATE
                publish_date = datetime.now()
                try:
                    created_at = twit.get('created_at', '').split(' ')[:4]
                    created_at = ' '.join(created_at)
                    publish_date = parser.parse(created_at)
                except:
                    pass
                Feed.objects.get_or_create(uid=twit_id, defaults={
                    'title': '@' + self.username,
                    'account_display_name': self.display_name,
                    'profile_img': profile_img,
                    'content': twit.get('text', ''),
                    'feeds_type': feeds_types.TWITTER,
                    'media_url': media_url,
                    'publish_date': publish_date,
                })
        except Exception as e:
            print ('ERROR Loading Twitter Posts: %s' % e)
