# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-23 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20161205_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='Featured'),
        ),
    ]
