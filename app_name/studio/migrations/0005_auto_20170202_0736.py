# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 07:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0004_auto_20170201_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 2, 7, 36, 17, 847175)),
        ),
        migrations.AlterField(
            model_name='competition',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 2, 7, 36, 17, 848291)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 2, 7, 36, 17, 849275)),
        ),
    ]