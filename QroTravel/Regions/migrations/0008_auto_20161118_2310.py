# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-18 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Regions', '0007_auto_20161118_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionphoto',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_photos', to='Regions.Section', verbose_name='Section'),
        ),
    ]
