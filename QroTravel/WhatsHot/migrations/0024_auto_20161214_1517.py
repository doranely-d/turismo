# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-14 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WhatsHot', '0023_auto_20161212_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('order',), 'verbose_name': 'Filter', 'verbose_name_plural': 'Filters'},
        ),
    ]
