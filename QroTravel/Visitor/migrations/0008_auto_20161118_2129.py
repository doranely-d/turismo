# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-18 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visitor', '0007_auto_20161118_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='queretarolanding',
            name='faqs_text_en',
            field=models.TextField(blank=True, verbose_name='FAQs text'),
        ),
        migrations.AddField(
            model_name='queretarolanding',
            name='faqs_text_fr',
            field=models.TextField(blank=True, verbose_name='FAQs text'),
        ),
    ]
