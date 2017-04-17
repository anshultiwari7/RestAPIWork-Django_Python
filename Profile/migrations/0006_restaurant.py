# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-04 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_auto_20160926_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('locality', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('country_id', models.CharField(max_length=10)),
                ('zipcode', models.CharField(default=-1, max_length=20)),
                ('average_cost_for_two', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=20)),
                ('menu_url', models.CharField(max_length=300)),
                ('aggregate_rating', models.CharField(max_length=20)),
                ('rating_text', models.CharField(max_length=300)),
                ('votes', models.CharField(max_length=100)),
                ('cuisines', models.CharField(max_length=50)),
            ],
        ),
    ]