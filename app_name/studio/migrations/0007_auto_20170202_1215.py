# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0006_auto_20170202_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='competition',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]