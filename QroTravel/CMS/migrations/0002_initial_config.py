# -*- coding: utf-8 -*-
from django.db import models, migrations

def get_or_create_contact(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Contact = apps.get_model("CMS", "Contact")
    try:
        contact = Contact.objects.get()
    except:
        contact = Contact()
        contact.save()


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(get_or_create_contact),
    ]
