# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-18 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0003_auto_20161018_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_fr',
        ),
    ]
