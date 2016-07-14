# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 13:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum', '0023_auto_20160712_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='author',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resource',
            name='shared',
            field=models.BooleanField(default=False),
        ),
    ]
