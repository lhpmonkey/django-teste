# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 22:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171026_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_published_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 26, 20, 2, 43, 267730)),
        ),
    ]
