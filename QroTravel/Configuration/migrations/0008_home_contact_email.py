# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-16 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0007_auto_20161207_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Contact Email'),
        ),
    ]
