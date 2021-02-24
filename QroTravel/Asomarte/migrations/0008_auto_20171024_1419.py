# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-24 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asomarte', '0007_metafields_translate'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='magazine_image_alt_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='magazine_image_alt_text_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='magazine_image_alt_text_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='video',
            name='image_alt_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='video',
            name='image_alt_text_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='video',
            name='image_alt_text_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
    ]
