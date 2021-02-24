# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-22 16:45
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0011_home_privacy_policy_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='privacy_policy_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='privacy policy'),
        ),
        migrations.AddField(
            model_name='home',
            name='privacy_policy_fr',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='privacy policy'),
        ),
        migrations.AddField(
            model_name='home',
            name='transparency',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Transparency'),
        ),
        migrations.AddField(
            model_name='home',
            name='transparency_banner_image',
            field=models.ImageField(blank=True, upload_to=b'transparency_images', verbose_name='Transparency banner Image'),
        ),
        migrations.AddField(
            model_name='home',
            name='transparency_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Transparency'),
        ),
        migrations.AddField(
            model_name='home',
            name='transparency_fr',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Transparency'),
        ),
        migrations.AlterField(
            model_name='home',
            name='error_banner_image',
            field=models.ImageField(blank=True, upload_to=b'configuration_images', verbose_name='Error banner Image'),
        ),
        migrations.AlterField(
            model_name='home',
            name='privacy_policy',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='privacy policy'),
        ),
        migrations.AlterField(
            model_name='home',
            name='privacy_policy_banner_image',
            field=models.ImageField(blank=True, upload_to=b'configuration_images', verbose_name='Privacy policy banner Image'),
        ),
        migrations.AlterField(
            model_name='home',
            name='search_banner_image',
            field=models.ImageField(blank=True, upload_to=b'configuration_images', verbose_name='Search banner Image'),
        ),
        migrations.AlterField(
            model_name='home',
            name='search_subtitle',
            field=models.CharField(blank=True, max_length=255, verbose_name='Search subtitle'),
        ),
        migrations.AlterField(
            model_name='home',
            name='search_subtitle_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Search subtitle'),
        ),
        migrations.AlterField(
            model_name='home',
            name='search_subtitle_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Search subtitle'),
        ),
        migrations.AlterField(
            model_name='home',
            name='search_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Search title'),
        ),
        migrations.AlterField(
            model_name='home',
            name='search_title_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Search title'),
        ),
        migrations.AlterField(
            model_name='home',
            name='search_title_fr',
            field=models.CharField(blank=True, max_length=255, verbose_name='Search title'),
        ),
    ]
