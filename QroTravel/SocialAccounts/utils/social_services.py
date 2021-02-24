from SocialAccounts.models import *


def load_social_posts():
    for twitter_account in TwitterAccount.objects.all():
        twitter_account.load_posts()
    for instagram_account in InstagramAccount.objects.all():
        instagram_account.load_posts()
    for facebook_account in FacebookAccount.objects.all():
        facebook_account.load_posts()
