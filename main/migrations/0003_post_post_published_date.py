# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 22:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_published_date',
            field=models.CharField(default=datetime.datetime(2017, 10, 26, 22, 0, 15, 628009, tzinfo=utc), max_length=50),
        ),
    ]
