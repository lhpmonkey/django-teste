# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 22:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_published_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 26, 22, 1, 25, 214281, tzinfo=utc)),
        ),
    ]
