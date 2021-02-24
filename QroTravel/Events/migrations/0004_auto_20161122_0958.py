# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-22 09:58
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_auto_20161116_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='event',
            name='longitude',
        ),
        migrations.AddField(
            model_name='event',
            name='position',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42, null=True, verbose_name='position'),
        ),
    ]
