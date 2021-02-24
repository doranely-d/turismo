# -*- coding: utf-8 -*-
from django.db import models, migrations


def get_or_create_landing(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    GastronomyLanding = apps.get_model("Gastronomy", "GastronomyLanding")
    try:
        landing = GastronomyLanding.objects.get()
    except:
        landing = GastronomyLanding()
        landing.save()


class Migration(migrations.Migration):

    dependencies = [
        ('Gastronomy', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(get_or_create_landing),
    ]
