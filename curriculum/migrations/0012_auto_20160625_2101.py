# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0011_auto_20160625_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='content',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]
