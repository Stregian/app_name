# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 17:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 1, 17, 48, 22, 592609)),
        ),
        migrations.AddField(
            model_name='competition',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 1, 17, 48, 22, 593185)),
        ),
        migrations.AddField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 1, 17, 48, 22, 593727)),
        ),
    ]
