# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-19 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WhatsHot', '0012_auto_20161019_1614'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Configuration',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=1, max_length=255, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='banner_image',
            field=models.ImageField(default=1, upload_to=b'sec_banner_image', verbose_name='banner image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.CharField(default=1, max_length=255, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='banner_image',
            field=models.ImageField(upload_to=b'cat_banner_image', verbose_name='banner image'),
        ),
    ]
