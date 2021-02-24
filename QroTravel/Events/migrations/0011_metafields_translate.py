# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-28 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0010_metafields'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='meta_description_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='meta_description_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='meta_keywords_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='meta_keywords_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='event',
            name='meta_description_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='event',
            name='meta_description_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='event',
            name='meta_keywords_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='event',
            name='meta_keywords_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Keywords'),
        ),
    ]
