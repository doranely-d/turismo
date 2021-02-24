# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-10 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WhatsHot', '0030_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='categories',
        ),
        migrations.AddField(
            model_name='card',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='WhatsHot.Category', verbose_name='categories'),
            preserve_default=False,
        ),
    ]
