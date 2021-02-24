# -*- coding: utf-8 -*-
from django.db import models, migrations

def get_or_create_configuration(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    FacebookConfiguration = apps.get_model("SocialAccounts", "FacebookConfiguration")
    try:
        config = FacebookConfiguration.objects.get()
    except:
        config = FacebookConfiguration()
        config.save()


class Migration(migrations.Migration):

    dependencies = [
        ('SocialAccounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(get_or_create_configuration),
    ]
