# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0011_auto_20161021_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelstation',
            name='Latitude',
            field=models.DecimalField(decimal_places=82, max_digits=152),
        ),
        migrations.AlterField(
            model_name='fuelstation',
            name='Longitude',
            field=models.DecimalField(decimal_places=82, max_digits=152),
        ),
    ]
