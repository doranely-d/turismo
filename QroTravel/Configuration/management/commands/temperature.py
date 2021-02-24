from django.core.management.base import BaseCommand, CommandError

from Configuration.utils import temperature_services


class Command(BaseCommand):

    def handle(self, *args, **options):
        temperature_services.load_temperature()
