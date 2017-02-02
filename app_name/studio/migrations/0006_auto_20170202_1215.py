# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0005_auto_20170202_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 2, 12, 15, 3, 428703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='competition',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 2, 12, 15, 3, 429363, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]