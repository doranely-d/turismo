# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-01 12:56
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WhatsHot', '0019_auto_20161123_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='card',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='card',
            name='description_fr',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='card',
            name='subtitle',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, verbose_name='sub title'),
        ),
        migrations.AlterField(
            model_name='card',
            name='subtitle_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, verbose_name='sub title'),
        ),
        migrations.AlterField(
            model_name='card',
            name='subtitle_fr',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, verbose_name='sub title'),
        ),
    ]
