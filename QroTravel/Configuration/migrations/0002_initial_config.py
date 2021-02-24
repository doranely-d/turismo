# -*- coding: utf-8 -*-
from django.db import models, migrations

def get_or_create_configuration(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Home = apps.get_model("Configuration", "Home")
    try:
        config = Home.objects.get()
    except:
        config = Home()
        config.save()


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(get_or_create_configuration),
    ]
