# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-14 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0008_auto_20161201_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='excerpt',
            field=models.TextField(verbose_name='sub title'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='excerpt_en',
            field=models.TextField(verbose_name='sub title'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='excerpt_fr',
            field=models.TextField(verbose_name='sub title'),
        ),
    ]
