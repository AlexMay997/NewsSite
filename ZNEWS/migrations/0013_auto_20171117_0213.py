# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZNEWS', '0012_newspost_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='post_category',
            field=models.CharField(choices=[('ECO', 'Economics'), ('WRD', 'World'), ('AUT', 'Auto'), ('PPL', 'People'), ('TCH', 'Tech'), ('SPR', 'Sport'), ('CBS', 'Cybersport'), ('RLT', 'Realty'), ('BSN', 'Business'), ('SCY', 'Society'), ('ACS', 'Accidents'), ('OTR', 'Other')], default='OTR', max_length=3),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='post_source',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
