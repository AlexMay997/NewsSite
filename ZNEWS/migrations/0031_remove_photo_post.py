# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZNEWS', '0030_remove_category_category_posts_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='post',
        ),
    ]
