from django.utils.translation import ugettext_lazy as _


TWITTER = 'twitter'
INSTAGRAM = 'instagram'
FACEBOOK = 'facebook'

FEEDS_TYPE_CHOICES = (
    (TWITTER, _('twitter')),
    (INSTAGRAM, _('instagram')),
    (FACEBOOK, _('facebook')),
)
