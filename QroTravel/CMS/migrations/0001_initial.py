# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-25 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title')),
                ('excerpt', models.TextField(verbose_name='Excerpt')),
                ('excerpt_en', models.TextField(verbose_name='Excerpt')),
                ('excerpt_fr', models.TextField(verbose_name='Excerpt')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_fr', models.TextField(verbose_name='Description')),
                ('description_en', models.TextField(verbose_name='Description')),
                ('banner_image', models.ImageField(upload_to=b'contact', verbose_name='Banner Image')),
                ('address', models.TextField(verbose_name='Address')),
                ('web_site', models.CharField(blank=True, max_length=255, verbose_name='Web Site')),
                ('contact_email', models.EmailField(blank=True, max_length=254, verbose_name='Contact Email')),
                ('instagram_url', models.URLField(blank=True, max_length=255, verbose_name='Instagram url')),
                ('twitter_url', models.URLField(blank=True, max_length=255, verbose_name='Twitter url')),
                ('facebook_url', models.URLField(blank=True, max_length=255, verbose_name='Facebook url')),
                ('phone_1', models.CharField(blank=True, max_length=15, verbose_name='Phone 1')),
                ('phone_2', models.CharField(blank=True, max_length=15, verbose_name='Phone 2')),
                ('phone_3', models.CharField(blank=True, max_length=15, verbose_name='Phone 3')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='longitude')),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=255, verbose_name='Title')),
                ('link', models.URLField(max_length=255, verbose_name='Link')),
                ('image', models.ImageField(upload_to=b'inspiration', verbose_name='Image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
            options={
                'verbose_name': 'Inspiration',
                'verbose_name_plural': 'Inspirations',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title')),
                ('link', models.URLField(max_length=255, verbose_name='Link')),
                ('banner_image', models.ImageField(upload_to=b'banners', verbose_name='Banner Image')),
                ('button_image_white', models.ImageField(blank=True, upload_to=b'banners', verbose_name='Button icon white')),
                ('button_image_color', models.ImageField(blank=True, upload_to=b'banners', verbose_name='Button icon color')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Order')),
                ('display', models.BooleanField(default=True, verbose_name='Display')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
    ]
