# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZNEWS', '0029_auto_20171211_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_posts_counter',
        ),
    ]
