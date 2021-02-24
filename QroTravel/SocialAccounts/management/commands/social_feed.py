from django.core.management.base import BaseCommand, CommandError

from SocialAccounts.utils.social_services import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_social_posts()
