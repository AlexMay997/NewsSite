# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZNEWS', '0024_auto_20171201_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_posts_counter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
