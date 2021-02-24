# -*- coding: utf-8 -*-
from django.db import models, migrations

def get_or_create_configuration(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Configuration = apps.get_model("Visitor", "Configuration")
    try:
        config = Configuration.objects.get()
    except:
        config = Configuration()
        config.save()


def get_or_create_landing(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    QueretaroLanding = apps.get_model("Visitor", "QueretaroLanding")
    try:
        landing = QueretaroLanding.objects.get()
    except:
        landing = QueretaroLanding()
        landing.save()


class Migration(migrations.Migration):

    dependencies = [
        ('Visitor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(get_or_create_configuration),
        migrations.RunPython(get_or_create_landing),
    ]
