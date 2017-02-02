# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 14:38
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170202_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=100, populate_from='name', unique=True),
        ),
    ]