# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170514_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pseudo', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=42)),
                ('adresse', models.CharField(max_length=42)),
                ('mail', models.CharField(max_length=42)),
                ('tel', models.IntegerField()),
                ('motdpass', models.CharField(max_length=42)),
            ],
        ),
    ]
