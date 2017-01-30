# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=50)),
                ('award_year', models.IntegerField()),
                ('award_project', models.CharField(max_length=100)),
                ('award_project_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_name', models.CharField(max_length=100)),
                ('competition_result', models.CharField(max_length=50)),
                ('competition_year', models.IntegerField()),
                ('competition_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_name', models.CharField(max_length=200)),
                ('publication_year', models.IntegerField()),
                ('publication_url', models.URLField()),
            ],
        ),
    ]
