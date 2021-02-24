# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-05 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regions', '0011_auto_20161201_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='sub_regions_sub_heading',
            field=models.TextField(blank=True, verbose_name='Sub Regions Sub Heading'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='sub_regions_sub_heading_en',
            field=models.TextField(blank=True, verbose_name='Sub Regions Sub Heading'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='sub_regions_sub_heading_fr',
            field=models.TextField(blank=True, verbose_name='Sub Regions Sub Heading'),
        ),
    ]
