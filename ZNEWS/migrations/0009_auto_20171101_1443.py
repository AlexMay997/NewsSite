# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZNEWS', '0008_remove_newspost_can_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='post_comments',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='post_photos',
        ),
        migrations.AddField(
            model_name='comment',
            name='answer_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZNEWS.Comment'),
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ZNEWS.NewsPost'),
        ),
    ]
