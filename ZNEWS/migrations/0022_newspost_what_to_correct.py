# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZNEWS', '0021_auto_20171120_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='what_to_correct',
            field=models.TextField(blank=True, null=True),
        ),
    ]
