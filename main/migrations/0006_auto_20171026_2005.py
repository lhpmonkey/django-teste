# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171026_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
