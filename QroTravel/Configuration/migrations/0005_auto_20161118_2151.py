# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-18 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0004_auto_20161118_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='search_banner_image',
            field=models.ImageField(default=1, upload_to=b'contact', verbose_name='Search banner Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='search_subtitle',
            field=models.CharField(default=1, max_length=255, verbose_name='Search subtitle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='search_subtitle_en',
            field=models.CharField(default=1, max_length=255, verbose_name='Search subtitle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='search_subtitle_fr',
            field=models.CharField(default=1, max_length=255, verbose_name='Search subtitle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='search_title',
            field=models.CharField(default=1, max_length=255, verbose_name='Search title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='search_title_en',
            field=models.CharField(default=1, max_length=255, verbose_name='Search title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='search_title_fr',
            field=models.CharField(default=1, max_length=255, verbose_name='Search title'),
            preserve_default=False,
        ),
    ]
