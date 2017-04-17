# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-24 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
                ('dob', models.DateTimeField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('register_time', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=100)),
                ('friends', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='f_userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile'),
        ),
    ]
