# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZNEWS', '0023_auto_20171127_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='post_content_photos',
        ),
        migrations.AlterField(
            model_name='newspost',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
