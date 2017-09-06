# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-06 16:11
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ToDolist', '0003_auto_20170905_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 6, 19, 11, 21, 861032)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.date(2017, 9, 6)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 6, 19, 11, 21, 861053)),
        ),
    ]
