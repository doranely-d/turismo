# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-24 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0012_auto_20171024_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_alt_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt Text'),
        ),
        migrations.AddField(
            model_name='event',
            name='image_alt_text_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt Text'),
        ),
        migrations.AddField(
            model_name='event',
            name='image_alt_text_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt Text'),
        ),
    ]
