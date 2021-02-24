# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-04 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regions', '0003_section_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configuration',
            options={'verbose_name': 'Region Guide Configuration'},
        ),
        migrations.AlterField(
            model_name='section',
            name='banner_image',
            field=models.ImageField(upload_to=b'region_section_banner', verbose_name='Banner image'),
        ),
    ]
