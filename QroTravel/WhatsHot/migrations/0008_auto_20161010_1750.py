# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-10 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WhatsHot', '0007_auto_20161010_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='main_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='main_sections', to='WhatsHot.Category', verbose_name='main category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='sections', to='WhatsHot.Category', verbose_name='category'),
        ),
    ]
