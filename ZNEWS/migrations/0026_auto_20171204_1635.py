# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZNEWS', '0025_category_category_posts_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_posts_counter',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
