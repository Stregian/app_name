# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 12:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_extensions.db.fields
import projects.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=projects.models.image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The name of this project', max_length=100)),
                ('location', models.CharField(default='', max_length=50)),
                ('information', models.TextField()),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=100, populate_from='title', unique=True)),
                ('date', models.DateField(default=datetime.datetime(2017, 2, 2, 12, 10, 2, 339333, tzinfo=utc))),
                ('year', models.IntegerField(choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=datetime.datetime(2017, 2, 2, 12, 10, 2, 339359, tzinfo=utc))),
                ('categories', models.ManyToManyField(to='projects.Category')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_image', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='category',
            name='fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_category', to='projects.Project'),
        ),
    ]
