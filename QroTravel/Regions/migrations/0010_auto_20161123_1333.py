# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-23 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regions', '0009_auto_20161122_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='position',
        ),
        migrations.AddField(
            model_name='section',
            name='google_maps',
            field=models.TextField(blank=True, help_text='Visit maps.google.com and copy the iframe', verbose_name='Google Maps Iframe'),
        ),
    ]
