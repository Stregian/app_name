# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20170202_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 2, 12, 15, 19, 497656, tzinfo=utc)),
        ),
    ]