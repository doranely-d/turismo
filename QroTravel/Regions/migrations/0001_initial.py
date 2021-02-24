# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Description')),
                ('subtitle_fr', models.TextField(verbose_name='Description')),
                ('subtitle_en', models.TextField(verbose_name='Description')),
                ('banner_image', models.ImageField(upload_to=b'regions_banner', verbose_name='Banner image')),
                ('sub_regions_heading', models.TextField(blank=True, verbose_name='Sub Regions Heading')),
                ('sub_regions_heading_fr', models.TextField(blank=True, verbose_name='Sub Regions Heading')),
                ('sub_regions_heading_en', models.TextField(blank=True, verbose_name='Sub Regions Heading')),
                ('sub_regions_image', models.ImageField(upload_to=b'sub_regions_image', verbose_name='Sub Regions image')),
            ],
            options={
                'verbose_name': 'Visitor Guide Configuration',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('slug_en', models.SlugField(max_length=255, verbose_name='slug')),
                ('slug_fr', models.SlugField(max_length=255, verbose_name='slug')),
                ('title_color', models.CharField(help_text='Hexadecimal color #000000', max_length=7, verbose_name='Title Color')),
                ('sub_title', models.TextField(verbose_name='Sub Title')),
                ('sub_title_en', models.TextField(verbose_name='Sub Title')),
                ('sub_title_fr', models.TextField(verbose_name='Sub Title')),
                ('heading', models.TextField(verbose_name='Heading')),
                ('heading_en', models.TextField(verbose_name='Heading')),
                ('heading_fr', models.TextField(verbose_name='Heading')),
                ('sub_heading', models.TextField(verbose_name='Sub Heading')),
                ('sub_heading_en', models.TextField(verbose_name='Sub Heading')),
                ('sub_heading_fr', models.TextField(verbose_name='Sub Heading')),
                ('extra_data', models.TextField(verbose_name='Extra Data')),
                ('extra_data_fr', models.TextField(verbose_name='Extra Data')),
                ('extra_data_en', models.TextField(verbose_name='Extra Data')),
                ('banner_image', models.ImageField(upload_to=b'region_banner', verbose_name='Banner image')),
                ('sub_banner_image', models.ImageField(upload_to=b'sub_region_banner', verbose_name='Sub Banner image')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title')),
                ('sub_title', models.TextField(verbose_name='Sub Title')),
                ('sub_title_en', models.TextField(verbose_name='Sub Title')),
                ('sub_title_fr', models.TextField(verbose_name='Sub Title')),
                ('sub_heading', models.TextField(verbose_name='Sub Heading')),
                ('sub_heading_en', models.TextField(verbose_name='Sub Heading')),
                ('sub_heading_fr', models.TextField(verbose_name='Sub Heading')),
                ('banner_image', models.ImageField(upload_to=b'visitor_section_banner', verbose_name='Banner image')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='Regions.Region')),
            ],
            options={
                'verbose_name': 'Regions Section',
                'verbose_name_plural': 'Regions Sections',
            },
        ),
    ]
