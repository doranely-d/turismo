# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-24 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regions', '0022_metafields_translate'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='sub_regions_image_alt_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='sub_regions_image_alt_text_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='sub_regions_image_alt_text_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='region',
            name='sub_banner_image_alt_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='region',
            name='sub_banner_image_alt_text_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='region',
            name='sub_banner_image_alt_text_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='sectionphoto',
            name='alt_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='sectionphoto',
            name='alt_text_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
        migrations.AddField(
            model_name='sectionphoto',
            name='alt_text_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alt text'),
        ),
    ]
