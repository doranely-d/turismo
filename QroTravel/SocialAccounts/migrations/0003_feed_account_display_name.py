# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-11 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialAccounts', '0002_initial_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='account_display_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Account display name'),
        ),
    ]
